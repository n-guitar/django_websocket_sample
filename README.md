# django3.1 ASGI uvicorn websocket sample

# sw version
```bash
$ python -V
Python 3.8.0
```

# memo
```bash
$ python -m venv env
$ source env/bin/activate
$ pip install django==3.1.3
$ pip install uvicorn
$ pip install websockets
$ uvicorn config.asgi:application
```

# branch
|branch name|overview|
|---|---|
|[simple-websocket-v0.1.0](https://github.com/n-guitar/django_websocket_sample/tree/simple-websocket-v0.1.0)|most simple websocket|