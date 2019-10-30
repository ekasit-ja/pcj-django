# pcj-django
This is development and deployment note for future use.

development is conducted on Windows 10.  use Ubuntu CLI to work with UNIX command in Windows environment.
1. install Python version 3 (note that command will be "python3" not just "python")
2. use "pip3" command for installing packages (not "pip")
3. folder structure will be like below (not mentioned folders are auto-generated)

project folder
│
│───"source" (source code folder)
│   │
│   │ pip_packages.txt (file contains all required packages)
│   │
│   └───"static_dev" (actual static file for development)
│
└───"static" (for gathering static file via command "python manage.py collectstatic")
│
│───"upload" (for uploaded files via admin page or CKEditor)

to run development server, we must use virtual environment by
1. "cd" to project folder first
2. then "source bin/active"
   *if this is first run, execute "pip install -r requirements.txt" to install all required packages*
3. then "cd source"
   *if this is first run, execute "python manage.py collectstatic" to gather all static files into "static" folder*
4. then "python manage.py runserver" and webpage can now be accessed via "localhost:8000"
