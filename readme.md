# Django Blog
An example Django site by Michal Dabski

This project's purpose is to showcase main features for Django framework and highlight the ease of bootstrapping a simple blog.
1. Models
2. Admin page
3. Views (list, detail, form)
4. Templates 
5. Tests

## Setup
Follow these steps to setup and run the project
### Install
To get the project to work in a virtual environment:
```bash
virtualenv .
source bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
./manage.py createsuperuser
```
### Get started
Visit http://localhost:8000/admin to login and create Autors and Articles.

Note: As this is just an example project, login page is not implemented for regular users, [Django admin login](http://localhost:8000/) page can be used as long as the user account is staff or superuser.
