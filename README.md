# pcj-django

### This is development and deployment note for future use.

### Problem on Cent OS 7 with SQLite3 and mod-wsgi
Default python in Cent OS 7 persist to use Sqlite version **3.7.17** while Django version 2.2.x requires sqlite version **3.8.3 or higher**. Many attempts to install sqlite newer version succeeded at development level. However, it failed at deployment stage. As a result, the latest version of Django we can use is **2.1.x**.

EasyApache4 on Cent OS also prevents us to use normal version of Apache2 and mod_wsgi.  Experiment (customized) version of mod_wsgi for EasyApache4 is not working neither. Therefore, deploying Django using EasyApache4 is not possible.

Deployment option is narrowed to **NGINX**. After doing research, we chose **uWSGI** for middleware over GUnicorn because deployment tutorial and community on Cent OS prefers uWSGI to GUnicorn.

In conclusion, we use **NGINX** for web server (which will serve static files). NGINX will communicate **uWSGI** via unix socket to invoke callable object of **Django** for dynamic data.

---

### Development
Development is conducted on Windows 10. We use _Ubuntu_ CLI to work with UNIX command in Windows environment.
1. install **Python version 3** (note that command will be `python3` not just `python`)
2. use `pip3` command for installing packages (not `pip`)
3. use **Bitvise SSH Client** application for SSH and FTP to server
4. folder structure will be like below (not mentioned folders are auto-generated)

```
.                         # project folder
│
├── site                  # contains log, initiate, and socket file used in deployment
├── source                # source code folder
│   ├── ...
│   ├── static_dev        # contains actual static files used in development
│   └── pip_packages.txt  # file containing all required python packages
├── static                # for gathering all static files via command "python3 manage.py collectstatic"
├── upload                # contains uploaded files via admin page or CKEditor
└── venv                  # contains virtual environment files
```

---

### Preparation for deployment
**Do NOT place project folder in** `/root`.  Place somewhere else like `/home/ekasit` (in this case). We will not give NGINX permission to access root folder.
1. First of all, create project folder with `mkdir pcj-django && cd pcj-django`
2. execute `mkdir source static upload site`
   - if this is first run, install python virtual environment executing `pip3 install virtualenv`
   - also copy everything into `upload` folder.  We use SQLite database so the data is already in repository.
3. execute `virtualenv -p python3 venv` to create python virtual environment
4. then `source venv/bin/activate`
5. then `cd source`
   - if this is first run, execute `git clone https://github.com/ekasit-ja/pcj-django.git .` to clone source code first
   - then execute `pip3 install -r pip_packages.txt` to install all required packages
   - on **Cent OS**, there may be problem with installing **django-compressor** package.  Run below first to solve the issue.
     - `pip3 install rcssmin --install-option="--without-c-extensions"`
     - `pip3 install rjsmin --install-option="--without-c-extensions"`
   - then execute `python3 manage.py collectstatic` to gather all static files and put them into `static` folder
6. then `python3 manage.py runserver 0.0.0.0:8000`.  Note that this is remotely access to server.  127.0.0.1:8000 is **NOT** remotely accessible.

**Note that video elements are all non-seekable on Django development environment**

---

### Working with CLI
Note that Django is **NOT** working when we put the process into background.

---

## Deployment
1. `deactivate` virtual environment first
2. We install uWSGI globally with `pip3 install uwsgi`
3. create file `pcj.ini` (uWSGI initial file) in folder `site`
4. paste below configuration in the file
```
[uwsgi]
home = /home/ekasit/pcj-django/venv
chdir = /home/ekasit/pcj-django/source
wsgi-file = /home/ekasit/pcj-django/source/pcj/wsgi.py

http = 0.0.0.0:8000
#socket = /home/ekasit/pcj-django/site/tutorial.sock
#vacuum = true
#chown-socket = root:root
#chmod-socket = 666
#listen = 512
```
5. execute `sysctl -w net.core.somaxconn=512` to increase system request size (this is a test to fix 502 error when server is on for a long period of time) and add `net.core.somaxconn=512` to file `/etc/sysctl.conf` for permanent change the request size
6. execute `uwsgi tutorial.ini` and browse website to check if it is working or not. (static files will not be served at this point)
7. if everything is fine, comment line `http = 0.0.0.0:8000` and remove comment from the rest
8. create service file at `/etc/systemd/system/uwsgi.service` to enable us to use command `service uwsgi restart`. This service file will run uWSGI in emperor mode. (Emperor mode means uWSGI will restart automatically when initial file is modified.). Paste below code into the file.
```
[Unit]
Description=uWSGI service (in emporer mode) for www.pcjindustries.co.th run by Django

[Service]
ExecStartPre=/bin/bash -c 'mkdir -p /run/uwsgi; chown root:root /run/uwsgi'
ExecStart=/usr/local/bin/uwsgi --emperor /home/ekasit/pcj-django/site/pcj.ini
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```
9. execute `systemctl daemon-reload` to inform system there is change from service files
10. install NGINX with `yum install nginx`
11. configure NGINX at `/etc/nginx/nginx.conf` by comment server directive (see below)
```
...
    include /etc/nginx/conf.d/*.conf;

#    server {
#        listen       80 default_server;
#        listen       [::]:80 default_server;
#        ...
#    }
...
```
12. then add below code instead
```
server {
    # allow upload file as large up to 10M #
    client_max_body_size 10M;

    listen 80;
    server_name    pcjindustries.co.th www.pcjindustries.co.th server.pcjindustries.co.th;

    access_log     /home/ekasit/pcj-django/site/access.log;
    error_log      /home/ekasit/pcj-django/site/error.log;

    location = favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /home/ekasit/pcj-django/static/;
    }

    location /media/ {
        alias /home/ekasit/pcj-django/upload/;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/ekasit/pcj-django/site/tutorial.sock;
    }
}
```
13. check syntax with `nginx -t`
14. restart service to apply changes by `service nginx restart && service uwsgi restart`
15. browse to website to check if it is working

at this point, we can use `service [nginx, uwsgi] [start, stop, restart]`

---

### Set up auto-start at boot
1. execute `systemctl enable uwsgi.service nginx`
2. then `reboot` to restart server
3. then `service nginx status` and `service uwsgi status` and browse to the website to check if everything is working.

---

### SSL for https
We will use **certbot** software to handle **Let’s Encrypt** certificate automatically.
1. install certbot by executing `yum install certbot python2-certbot-nginx`
2. then `certbot --nginx` to let certbot configure NGINX automatically
3. certbot will put check key on `/root/static` by default (called webroot-path). However, we do not let nginx have root access.  So we have to change webroot-path by `certbot certonly --webroot -w /home/ekasit/pcj-django -d www.pcjindustries.co.th,pcjindustries.co.th,server.pcjindustries.co.th` then choose option 2 (renew and replace cert) (use only 1 -d to create just 1 domain for all 3 addresses. There should be only 1 certificate folder which is `www.pcjindustries.co.th`)
4. we have to force all `non-www` to `www` as well as provide `.well-known` path by changing below
```
location / {
    include uwsgi_params;
    uwsgi_pass unix:/home/ekasit/pcj-django/site/tutorial.sock;
}
```
to
```
location /.well-known/ {
    alias /home/ekasit/pcj-django/.well-known/;
}

location / {
    include uwsgi_params;
    uwsgi_pass unix:/home/ekasit/pcj-django/site/tutorial.sock;
}

if ($host = server.pcjindustries.co.th) {
    return 301 https://www.pcjindustries.co.th$request_uri;
} # managed by Certbot

if ($host = pcjindustries.co.th) {
    return 301 https://www.pcjindustries.co.th$request_uri;
} # managed by Certbot
```
5. in server directive which listen to port 80, change
```
server {
if ($host = www.pcjindustries.co.th) {
    return 301 https://$host$request_uri;
} # managed by Certbot


if ($host = server.pcjindustries.co.th) {
    return 301 https://$host$request_uri;
} # managed by Certbot


if ($host = pcjindustries.co.th) {
    return 301 https://$host$request_uri;
} # managed by Certbot
```
to
```
if ($host = www.pcjindustries.co.th) {
    return 301 https://www.pcjindustries.co.th$request_uri;
} # managed by Certbot


if ($host = server.pcjindustries.co.th) {
    return 301 https://www.pcjindustries.co.th$request_uri;
} # managed by Certbot


if ($host = pcjindustries.co.th) {
    return 301 https://www.pcjindustries.co.th$request_uri;
} # managed by Certbot
```
6. restart NGINX with `service nginx restart` and execute `certbot renew --dry-run` to check if renewal succeed or not.
7. set job to auto-renew certificate by executing `crontab -e`. cronjob file will be opened
8. then put `0 4 2 * * /usr/bin/certbot renew >> /home/ekasit/pcj-django/site/renew_cert.log 2>&1` on the last line. (it means every month, on 2nd day at 04.00, execute `certbot renew` and log it in that file either output is normal or error)

---

### Auto restart service
After long period of deployment time, service alawys crashes for unknown reason.  Therefore, we need to restart service automatically by `crontab`.  Thus set up to restart the service daily.
1. Open file `/var/spool/cron/root`
2. add `0 4 * * * /home/ekasit/pcj-django/source/daily_restart.sh >> /home/ekasit/pcj-django/site/daily_restart.log 2>&1` on the last line
3. save the file
4. change permission of `daily_restart.sh` file in source code folder to 744 (executable by owner)

---

### Before signing off & Every later update
1. Do not forget to change `DEBUG=False` in `settings.py`
2. execute `python3 manange.py collectstatic` (under virtual environment) to collect all updated static files
3. and restart both services with `service nginx restart && service uwsgi restart`
