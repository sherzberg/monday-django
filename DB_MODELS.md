DB Models
=========

Django's ORM has many useful features built in:

- One-to-one, one-to-many, many-to-many
- Bi-directional relationships
- Auto primary key
- Schema Generation
- Lazy evaluation
- REPL ORM shell

Setup
-----

Lets create the database with our current project by using a built in Django command:

```bash
vagrant@precise64~/monday-django/monday
$ python manage.py syncdb
```

Now lets see what sql was used to generate the schema:

```bash
vagrant@precise64~/monday-django/monday
$ python manage.py sql deployments
```

With the schema created, lets load some stock data:

```bash
vagrant@precise64~/monday-django/monday
$ python manage.py loaddata data.json
```

Querying
--------

```bash
vagrant@precise64~/monday-django/monday
$ python manage.py shell
Python 2.7.3 (default, Apr 10 2013, 06:20:15) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from deployments.models import *
>>> Code.objects.all()
[<Code: Code object>, <Code: Code object>]
>>> len(Code.objects.all())
2
>>> app1 = Code.objects.all()[0]
>>> app1.name
u'Flower'
>>> app1.application_set.all()
[]
```

Filtering
---------

```bash
```

Inserting
---------

```bash
>>> Code.objects.create(name='Test', repo='git@github.com/sherzberg/test.git')
<Code: Code object>
```

Updating
--------
