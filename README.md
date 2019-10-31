# pcj-django

### This is development and deployment note for future use.

#### Development is conducted on Windows 10.  use _Ubuntu_ CLI to work with UNIX command in Windows environment.
1. install **Python version 3** (note that command will be `python3` not just `python`)
2. use `pip3` command for installing packages (not `pip`)
3. use **Bisvise SSH Client** application for terminal and FTP to server
4. folder structure will be like below (not mentioned folders are auto-generated)

```
.                           # project folder
├── ...
│
├── source                  # source code folder
│   │
│   ├── ...
│   │
│   ├── pip_packages.txt    # file containing all required packages
│   │
│   └── static_dev          # folder containing actual static files for development
│
├── static                  # for gathering static files via command "python3 manage.py collectstatic"
│
└── upload                  # for uploaded files via admin page or CKEditor
```
---

#### Problem with SQLite3 on Cent OS 7
Default python in Cent OS 7 persist to use Sqlite version **3.7.17** while django requires Sqlite version **3.8.3 or higher**.  Ordinary update will not change version acknowledgded by python at all.  Therefore, follow this [instruction](http://www.djaodjin.com/blog/django-2-2-with-sqlite-3-on-centos-7.blog.html) on how to solve this issue.

Be sure to add `export LD_LIBRARY_PATH=/usr/local/lib` into `~/.bashrc` profile and restart terminal so when we execute `python3 -c "import sqlite3; print(sqlite3.sqlite_version)"`, it will return a newer version of sqlite.

---

#### Initiating development server instruction (using python virtual environment is recommended)
1. `cd` to project folder first
   - if this is first run, install python virtual environment first by executing `pip3 install virtualenv`
   - then execute `virtualenv -p python3 .` to create python virtual environment first
   - then execute `mkdir static`
   - and execute `mkdir upload`
   - also copy everything into **upload** folder.  We use SQLite database so the data is already in repository.
2. then `source bin/activate`
   - if this is first run, execute `git clone https://github.com/ekasit-ja/pcj-django.git source` to clone source code first
3. then `cd source`
   - in case of **Cent OS**, there may be problem with installing **django-compressor** package.  Run below first to solve the issue.
     - `pip3 install rcssmin --install-option="--without-c-extensions"`
     - `pip3 install rjsmin --install-option="--without-c-extensions"`
   - if this is first run, execute `pip3 install -r pip_packages.txt` to install all required packages
   - then execute `python3 manage.py collectstatic` to gather all static files and put them into **static** folder
4. then `python3 manage.py runserver 0.0.0.0:8000`.  Note that this is remotely access to server.  127.0.0.1:8000 is **NOT** remotely accessible.

**Note that video elements are all non-seekable on Django development**

---

#### Working with CLI
- we can use `Ctrl + Z` to put a process into background
- use `jobs` to see all background processes
- use `fg` to bring a background process to foreground.
- use `fg %#` in case there are more than one background processes

#### Working with GIT
Without `python3 manage.py makemigrations` and `python3 manage.py migrate` command on remote server, code still works fine.  However, migration files will be modified automatically when we run the server.  Use `git reset --hard` to discard all changes.  Then use `git pull` to update source code from GIT.

---
