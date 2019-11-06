# pcj-django

### This is development and deployment note for future use.

### Problem on Cent OS 7 with SQLite3 and mod-wsgi
Default python in Cent OS 7 persist to use Sqlite version **3.7.17** while django version 2.2.x requires sqlite version **3.8.3 or higher**. Many attempts to install sqlite newer version succeeded at development level. However, it failed at deployment stage. As a result, the latest version of django we can use is **2.1.x**.

EasyApache4 on Cent OS also prevents us to use normal version of Apache2 and mod_wsgi.  Experiment (customized) version of mod_wsgi for EasyApache4 is not working neither. Therefore, deploying django using EasyApache4 is not possible.

Deployment option is narrowed to **NGINX**. After doing research, we chose **uWSGI** for middleware over GUnicorn because deployment tutorial and community on Cent OS prefers uWSGI to GUnicorn.

In conclusion, we use **NGINX** for web server (which will serve static files). NGINX will communicate **uWSGI** via unix socket to invoke callable object of **Django** for dynamic data.

---

### Development
Development is conducted on Windows 10. We use _Ubuntu_ CLI to work with UNIX command in Windows environment.
1. install **Python version 3** (note that command will be `python3` not just `python`)
2. use `pip3` command for installing packages (not `pip`)
3. use **Bisvise SSH Client** application for SSH and FTP to server
4. folder structure will be like below (not mentioned folders are auto-generated)

```
.                           # project folder
│
├── source                  # source code folder
│   │
│   ├── ...
│   ├── pip_packages.txt    # file containing all required python packages
│   └── static_dev          # contains actual static files used in development
├── ...
├── static                  # for gathering all static files via command "python3 manage.py collectstatic"
├── upload                  # contains uploaded files via admin page or CKEditor
├── venv                    # contains virtual environment files
└── site                    # contains log, initiate, and socket file used in deployment

```

---

### Preparation for deploment
1. First of all, create project folder with `mkdir pcj-django` and `cd pcj-django`
2. execute `mkdir source static upload site`
   - if this is first run, install python virtual environment executing `pip3 install virtualenv`
   - also copy everything into **upload** folder.  We use SQLite database so the data is already in repository.
3. execute `virtualenv -p python3 venv` to create python virtual environment
4. then `source venv/bin/activate`
   - if this is first run, execute `git clone https://github.com/ekasit-ja/pcj-django.git source` to clone source code first
   - then execute `pip3 install -r pip_packages.txt` to install all required packages
5. then `cd source`
```
   - in case of **Cent OS**, there may be problem with installing **django-compressor** package.  Run below first to solve the issue.
     - `pip3 install rcssmin --install-option="--without-c-extensions"`
     - `pip3 install rjsmin --install-option="--without-c-extensions"`
```
   - then execute `python3 manage.py collectstatic` to gather all static files and put them into **static** folder
6. then `python3 manage.py runserver 0.0.0.0:8000`.  Note that this is remotely access to server.  127.0.0.1:8000 is **NOT** remotely accessible.

**Note that video elements are all non-seekable on Django development environment**

---

### Working with CLI
Note that Django is **NOT** working when we put the process into background.

### Working with GIT
Without `python3 manage.py makemigrations` and `python3 manage.py migrate` command on remote server, code still works fine.  However, migration files will be modified automatically when we run the server.  Use `git reset --hard` to discard all changes.  Then use `git pull` to update source code from GIT.

---

## Deployment
Our server runs on **Cent OS** which already has **WHM, CPanel, and Apache2** (can be configured by Easy Apache 4 on WHM). Apache will serve all static files.  For dynamic file requests, Apache will invoke python via **mod-wsgi**.

- use `netstat -tulpn` to find out which service is listening to which port.

### Do not put anything in `root` folder.  Users do NOT have permission to access this folder at all.

1. install mod-wsgi by executing
```
yum install ea4-experimental
yum install ea-apache24-mod_wsgi
```
2. backup Apache config file `/etc/apache2/conf.d/includes/pre_virtualhost_global.conf` (default is empty file)
3. modified config file as below.

```
LoadModule wsgi_module /usr/lib64/apache2/modules/mod_wsgi.so
Listen 8000

<VirtualHost *:8000>

    ServerAdmin ekasit@pcjindustries.co.th
    DocumentRoot /var/www/html

    ServerName pcjindustries.co.th
    ServerAlias www.pcjindustries.co.th

    ErrorLog /pcj/pcj-django/error.log
    CustomLog /pcj/pcj-django/access.log combined

    <Directory /pcj/pcj-django/source/pcj>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess source python-home=/pcj/pcj-django python-path=/pcj/pcj-django/source
    WSGIProcessGroup source
    WSGIScriptAlias / /pcj/pcj-django/source/pcj/wsgi.py

</VirtualHost>

```

4. execute `apachectl configtest` to check correctness of config file
   - there may be a case that configuration on file directly is not acknowledged by Apache.  In such case, edit configuration on WHM via **Home > Service Configuration > Apache Configuration > Include Editor**.  Web interface will return any errors that may occurred.
5. execute `service httpd restart` (WHM interface have restart button in case modification is done on webpage)


 first tim run, `yum install ea-apache24-devel`
 then ,`pip3 install mod-wsgi`


### mod_wsgi is no hope. use NGINX and GUnicorn instead
### configuring gunicorn
1. `sudo apt-get install nginx`
2. `pip3 install gunicorn`
3. cd to folder containg `manage.py`
4. `gunicorn --bind 0.0.0.0:8000 pcj.wsgi:application` to check correctness
5. create file `gunicorn.service` in `/etc/systemd/system`
6. put below configuration
```
[Unit]
Description=gunicorn service
After=network.target

[Service]
User=chris
Group=www-data
WorkingDirectory=/home/chris/webapp/AWESOME_PROJECT/
ExecStart=/home/chris/webapp/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/chris/webapp/AWESOME_PROJECT/awesome.sock AWESOME.wsgi:application

[Install]
WantedBy=multi-user.target
```

### configuring nginx
1. goto folder `/etc/nginx/sites-available`
2. create file `pcj` (no extension) and put below data
```
server {
    listen 8000;
    server_name localhost;
    location = "/mnt/c/Users/Gaming PC/Desktop/trydjango/static/images" {access_log off;log_not_found off;}

    location = /static/ {
        root "/mnt/c/Users/Gaming PC/Desktop/trydjango/static";
    }
    location = /media/ {
        root "/mnt/c/Users/Gaming PC/Desktop/trydjango/upload";
    }

    location /some/path/ {
        proxy_pass http://localhost;
    }
}

```
3. `sudo ln -s /etc/nginx/sites-available/pcj /etc/nginx/sites-enabled`
4. `sudo nginx -t` to check configuration
5. `sudo service nginx restart`




1. `pip3 install uwsgi` install it globally
```
[uwsgi]
home = /home/ekasit/tutorial/venv
chdir = /home/ekasit/tutorial/django/tutorial
wsgi-file = /home/ekasit/tutorial/django/tutorial/tutorial/wsgi.py

socket = /home/ekasit/tutorial/site/tutorial.sock
vacuum = true
chown-socket = root:root
chmod-socket = 666

```
2. `uwsgi tutorial.ini`
3. `pkill -f uwsgi`

4. create file at `/etc/systemd/system/uwsgi.service` to start uWSGI automatically at boot in emperor mode. (Emperor mode means uWSGI will restart automatically when initial file is modified.)
```
[Unit]
Description=uWSGI service (in emporer mode) for www.pcjindustries.co.th run by Django

[Service]
ExecStartPre=/bin/bash -c 'mkdir -p /run/uwsgi; chown root:root /run/uwsgi'
ExecStart=/usr/local/bin/uwsgi --emperor /home/ekasit/tutorial/site/tutorial.ini
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target

```
4. `systemctl daemon-reload`
5. now we can execute `service uwsgi.service restart` `service uwsgi.service stop`


6. `yum install nginx`
7. edit `/etc/nginx/nginx.conf` by adding configuration in between of
```
...
include /etc/nginx/conf.d/*.conf;

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
      include /etc/nginx/conf.d/*.conf;

# add configuration here

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
...
```
8. add this
```
server {
    listen 8000;
    server_name pcjindustries.co.th www.pcjindustries.com;

    access_log      /home/ekasit/tutorial/site/logs/access.log;
    error_log       /home/ekasit/tutorial/site/logs/error.log;

    location = favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ekasit/tutorial/static;
    }

    location /media/ {
        root /home/ekasit/tutorial/upload;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/ekasit/tutorial/site/tutorial.sock;
    }

}
```
9. check syntax `nginx -t`
10. `service nginx restart && service uwsgi restart`
