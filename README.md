How to start
============

Set Flask Env viables, on windows, use export on Linux.

```
set FLASK_APP=flask_rest_psql_docker.app
set FLASK_ENV=development
```

Run `flask shell` and then,

```
>>> db.create_all()
>>> user = User(first='wally', last='west', job='the flash', shool='star labs', age=19)
>>> db.session.add(user)
>>> db.session.commit()
```

Start flask app with `flask run`, to view all your routes you can run `flask routes` 
and it will give you a map of all your routes.

PSQL Setup
============
Set `DATABASE_URI` environment variable, e.g. `postgresql://username:password@hostname:port/database`.