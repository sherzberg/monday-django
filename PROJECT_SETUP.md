Project Setup
=============

We are going to use Vagrant + Virtualbox to setup the Python/Django development environment so the dependencies are isolated from any other environment.

First checkout the repository:

```bash
sherzberg@tiblets~
$ git clone git@github.com:sherzberg/monday-django.git
```

Now fire up the vagrant instance:

```bash
sherzberg@tiblets~/monday-django
$ vagrant up
sherzberg@tiblets~/monday-django
$ vagrant ssh
```

Django Setup
------------

Django has some utility commands to help bootstrap the project. First install django:

```bash
vagrant@precise64~
$ sudo pip install django
vagrant@precise64~
$ cd monday-django
vagrant@precise64~/monday-django
$ django-admin.py startproject monday && cd monday
vagrant@precise64~/monday-django/monday
$ python manage.py runserver 0.0.0.0:8000
```

Now visit http://localhost:8000 on your host machine. Now while the django dev server is running, any changes to code will call a restart and changes can be viewed right away.

Take a look at the settings.py file in monday/monday/. All of the main settings for the django project are located here.

App Setup
---------

Django has a concept of reusable components called Apps. These apps can contain db models, views, templates, static files, and even settings. For the most part, apps are meant to be reusable for generic purposes. Lets make one:

```bash
vagrant@precise64~/monday-django/monday
$ django-admin.py startapp deployments
```

This will create a folder called _deployments_ and will contain models.py, test.py, and views.py.

If you want to see more project setup docs, look here https://docs.djangoproject.com/en/1.5/intro/tutorial01/
