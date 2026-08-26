# pcj-django

### This is development and deployment note for Ubuntu 24.04.4 LTS

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
   - if this is first run, install python virtual environment executing `pip3 install virtualenv` (Ubuntu will ask to use `apt` instead of installing with `pip` when not in virtual environment. Do so)
   - also copy everything into `upload` folder.  We use SQLite database so the data is already in repository.
3. execute `virtualenv -p python3 venv` to create python virtual environment
4. then `source venv/bin/activate`
5. then `cd source`
   - if this is first run, execute `git clone https://github.com/ekasit-ja/pcj-django.git .` to clone source code first
   - then execute `pip3 install -r pip_packages.txt` to install all required packages
   - then execute `python3 manage.py collectstatic` to gather all static files and put them into `static` folder
6. then `python3 manage.py runserver 0.0.0.0:8000`.  Do not forget to add IP address to `settings.py` file.

**Note that video elements are all non-seekable on Django development environment**

---

### Working with CLI
Note that Django is **NOT** working when we put the process into background.

---

## Deployment
1. `activate` virtual environment first
2. We install uWSGI in virtual environment with `pip3 install uwsgi`
3. create file `pcj.ini` (uWSGI initial file) in folder `site`
4. paste below configuration in the file
```
[uwsgi]
home = /home/ekasit/pcj-django/venv
chdir = /home/ekasit/pcj-django/source
wsgi-file = /home/ekasit/pcj-django/source/pcj/wsgi.py

http = 0.0.0.0:8000
#socket = /home/ekasit/pcj-django/site/pcjdjango.sock
#vacuum = true
#chown-socket = root:root
#chmod-socket = 666
#listen = 512
```
5. execute `uwsgi pcj.ini` and browse website to check if it is working or not. (static files will not be served at this point)
6. if everything is fine, comment line `http = 0.0.0.0:8000` and remove comment from the rest
7. create service file at `/etc/systemd/system/uwsgi.service` to enable us to use command `service uwsgi restart`. This service file will run uWSGI in emperor mode. (Emperor mode means uWSGI will restart automatically when initial file is modified.). Paste below code into the file.
```
[Unit]
Description=uWSGI service (in emporer mode) for www.pcjindustries.co.th run by Django

[Service]
ExecStartPre=/bin/bash -c 'mkdir -p /run/uwsgi; chown root:root /run/uwsgi'
ExecStart=/home/ekasit/pcj-django/venv/bin/uwsgi --emperor /home/ekasit/pcj-django/site/pcj.ini
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```
9. execute `systemctl daemon-reload` to inform system there is change from service files
10. install NGINX with `apt install nginx`
11. configure NGINX at by creating a file `/etc/nginx/sites-available/pcjindustries`
12. Put below code in `pcjindustries` file. Replace with actual IP address.
```
server {
    client_max_body_size 10M;

    listen 80;
    server_name pcjindustries.co.th www.pcjindustries.co.th;

    access_log /home/ekasit/pcj-django/site/access.log;
    error_log /home/ekasit/pcj-django/site/error.log;

    location = favicon.ico {
        access_log off;
        log_not_found off;
    }

    location /.well-known/acme-challenge/ {
        root /home/ekasit/pcj-django;
        try_files $uri =404;
    }

    location /static/ {
        alias /home/ekasit/pcj-django/static/;
    }

    location /media/ {
        alias /home/ekasit/pcj-django/upload/;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/ekasit/pcj-django/site/pcjdjango.sock;
    }
}
```
13. execute `ln -s /etc/nginx/sites-available/pcjindustries /etc/nginx/sites-enabled/pcjindustries`
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
1. install certbot by executing `apt install certbot python3-certbot-nginx`
2. then execute `certbot certonly --webroot -w /home/ekasit/pcj-django -d pcjindustries.co.th -d www.pcjindustries.co.th`


4. we have to force all `non-www` redirect to `www` and `http` redirect to `https`. We change entire `/etc/nginx/sites-available/pcjindustries` with below code
```
# HTTP → HTTPS + www
server {
    listen 80;
    server_name pcjindustries.co.th www.pcjindustries.co.th;

    # Allow Let's Encrypt ACME challenge
    location /.well-known/acme-challenge/ {
        root /home/ekasit/pcj-django;
        try_files $uri =404;
    }

    location / {
        return 301 https://www.pcjindustries.co.th$request_uri;
    }
}


# HTTPS non-www → HTTPS www
server {
    listen 443 ssl;
    server_name pcjindustries.co.th;

    ssl_certificate /etc/letsencrypt/live/pcjindustries.co.th/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/pcjindustries.co.th/privkey.pem;

    return 301 https://www.pcjindustries.co.th$request_uri;
}


# HTTPS www → Django
server {
    listen 443 ssl;
    server_name www.pcjindustries.co.th;

    client_max_body_size 10M;

    ssl_certificate /etc/letsencrypt/live/pcjindustries.co.th/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/pcjindustries.co.th/privkey.pem;

    access_log /home/ekasit/pcj-django/site/access.log;
    error_log /home/ekasit/pcj-django/site/error.log;

    location = favicon.ico {
        access_log off;
        log_not_found off;
    }

    # Allow Let's Encrypt ACME challenge
    location /.well-known/acme-challenge/ {
        root /home/ekasit/pcj-django;
        try_files $uri =404;
    }

    location /static/ {
        alias /home/ekasit/pcj-django/static/;
    }

    location /media/ {
        alias /home/ekasit/pcj-django/upload/;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/ekasit/pcj-django/site/pcjdjango.sock;
    }
}
```
5. restart NGINX with `service nginx restart` and execute `certbot renew --dry-run` to check if renewal succeed or not.
6. `certbot` already have timer to run `renew` by default twice a day. No need to do auto renewal code.

---

### Auto restart service
After long period of deployment time, service may crash for unknown reason.  Therefore, we need to restart service automatically by `crontab`.  Thus set up to restart the service daily.
1. set job to auto restart service by executing `crontab -e`. cronjob file will be opened
2. add `0 4 * * * (service nginx restart && service uwsgi restart) >> /home/ekasit/pcj-django/site/daily_restart.log 2>&1` on the last line
3. save the file (Ctrl+x then Ctrl+o)

---

### Before signing off & Every later update
1. Do not forget to change `DEBUG=False` in `/home/ekasit/pcj-django/source/pcj/settings.py`
2. execute `(cd /home/ekasit/pcj-django/source && /home/ekasit/pcj-django/venv/bin/django-admin compilemessages)` to update text file (May need to install `apt update && apt install gettext` if `GNU gettext tools` is not installed)
3. execute `(cd /home/ekasit/pcj-django/source && /home/ekasit/pcj-django/venv/bin/python manage.py collectstatic)` to collect all updated static files
4. and restart both services with `service nginx restart && service uwsgi restart`

### To use new SSL certificate on WHM
search for `Manage Service SSL Certificates`
