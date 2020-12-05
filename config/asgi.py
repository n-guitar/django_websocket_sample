import os

from django.core.asgi import get_asgi_application
from websocket.websocket import websocket_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django_application = get_asgi_application()

async def application(scope, receive, send):
    if scope['type'] == 'http':
        # # debug
        # print('-----asgi.py:django_application------')
        # # print('scope:',scope)
        # print('scope[\'type\']:',scope['type'])
        # print('scope[\'asgi\']:',scope['asgi'])
        # print('scope[\'http_version\']:',scope['http_version'])
        # print('scope[\'server\']:',scope['server'])
        # print('scope[\'client\']:',scope['client'])
        # print('scope[\'scheme\']:',scope['scheme'])
        # print('scope[\'method\']:',scope['method'])
        # print('scope[\'root_path\']:',scope['root_path'])
        # print('scope[\'path\']:',scope['path'])
        # print('scope[\'raw_path\']:',scope['raw_path'])
        # print('scope[\'query_string\']:',scope['query_string'])
        # print('scope[\'headers\']:',scope['headers'])
        # print('-----------------------------')
        await django_application(scope, receive, send)
    elif scope['type'] == 'websocket':
        print('----asgi.py:websocket_application----')
        # print('scope:',scope)
        print('scope[\'type\']:',scope['type'])
        print('scope[\'asgi\']:',scope['asgi'])
        print('scope[\'server\']:',scope['server'])
        print('scope[\'client\']:',scope['client'])
        print('scope[\'scheme\']:',scope['scheme'])
        print('scope[\'root_path\']:',scope['root_path'])
        print('scope[\'path\']:',scope['path'])
        print('scope[\'raw_path\']:',scope['raw_path'])
        print('scope[\'query_string\']:',scope['query_string'])
        print('scope[\'headers\']:',scope['headers'])
        print('-----------------------------')
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")