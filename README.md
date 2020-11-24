python -m venv env
source env/bin/activate
pip install django==3.1.3
env/bin/django-admin startproject config .
pip install uvicorn
uvicorn config.asgi:application
これだとwebsocketプロトコルが使えなくてerrになる
websocketが必要

pip install websockets
uvicorn config.asgi:application
