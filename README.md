# pcj-django
### This is development and deployment note for future use.

### Development is conducted on Windows 10.  use _Ubuntu_ CLI to work with UNIX command in Windows environment.
1. install **Python version 3** (note that command will be **python3** not just **python**)
2. use **pip3** command for installing packages (not **pip**)
3. folder structure will be like below (not mentioned folders are auto-generated)

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

### To run development server, we must use virtual environment by
1. `cd` to project folder first
   - if this is first run, execute `virtualenv -p python3 .` to create python virtual environment first
   - then execute `mkdir static`
   - and execute `mkdir upload`
   - also copy everything into **upload** folder.  We use SQLite database so the data is already in repository.
2. then `source bin/activate`
   - if this is first run, execute `git clone https://github.com/ekasit-ja/pcj-django.git source` to clone source code first
3. then `cd source`
   - in case of **Cent OS**, execute these first
     -`pip3 install rcssmin --install-option="--without-c-extensions"`
     -`pip3 install rjsmin --install-option="--without-c-extensions"`
   - if this is first run, execute `pip3 install -r pip_packages.txt` to install all required packages
   - then execute `python3 manage.py collectstatic` to acquire all static files into **static** folder
4. then `python3 manage.py runserver` and webpage can now be accessed via [localhost:8000](localhost:8000)
