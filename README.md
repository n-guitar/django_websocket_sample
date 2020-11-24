

python -m venv env
source env/bin/activate
pip install django==3.1.3
env/bin/django-admin startproject config .
pip install uvicorn
uvicorn config.asgi:application
# これだとwebsocketプロトコルが使えなくてerrになる
websocketが必要

pip install websockets
uvicorn config.asgi:application


参考サイト
https://dev.to/jaydenwindle/adding-websockets-to-your-django-app-with-no-extra-dependencies-2f6h
https://github.com/encode/uvicorn/issues/797