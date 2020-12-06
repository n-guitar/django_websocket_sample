from django.urls import resolve
from .connection import WebSocket

def websockets(django_application):
    async def asgi(scope, receive, send):
        # debug
        print('----websocket.py:websockets----')
        print('scope[\'server\']:',scope['server'])
        print('scope[\'client\']:',scope['client'])
        print('scope[\'scheme\']:',scope['scheme'])
        print('scope[\'path\']:',scope['path'])
        print('scope[\'raw_path\']:',scope['raw_path'])
        print('scope[\'query_string\']:',scope['query_string'])
        print('scope[\'headers\']:',scope['headers'])
        print('scope[\'headers[0][0].decode()\']:',scope['headers'][0][0].decode())
        print('-----------------------------')
        if scope['type'] == 'http':
            await django_application(scope, receive, send)
            return
            # websocketのものはすべて『websocket_application』になり、js側がどんなpathでアクセスしてきてもすべて同じwebsocketで受け付けることになる
        elif scope["type"] == "websocket":
            match = resolve(scope["raw_path"])
            await match.func(WebSocket(scope, receive, send), *match.args, **match.kwargs)
            # await websocket_application(scope, receive, send)
            return
        else:
            raise NotImplementedError(f"Unknown scope type {scope['type']}")
    return asgi