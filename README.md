# Django Channels Examples

Examples of asynchronous projects with Django Channels 2.

Use the pipenv tool

``` shellsession
$ pip install pipenv
$ pipenv install
```

Start the redis server (and make sure it is running in the background)

``` shellsession
$ redis-server
```

Now you need to enter the pipenv shell to run the examples:

``` shellsession
$ pipenv shell
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

You should see no notifications. Now open another browser window and log into Django admin. Add a new user. If you look
at the first browser windows, then you should see the new user notification.
