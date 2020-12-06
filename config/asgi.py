import os

from django.core.asgi import get_asgi_application
from websocket.websocket import websockets

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django_application = get_asgi_application()
# uvicorn config.asgi:application で指定する名前にする。
application = websockets(django_application)
