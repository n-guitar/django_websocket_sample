def websockets(django_application):
    async def asgi(scope, receive, send):
        # debug
        print('----websocket.py:websockets----')
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
        print('scope[\'headers[0][0].decode()\']:',scope['headers'][0][0].decode())
        print('-----------------------------')
        if scope['type'] == 'http':
            await django_application(scope, receive, send)
            return
            # websocketのものはすべて『websocket_application』になり、js側がどんなpathでアクセスしてきてもすべて同じwebsocketで受け付けることになる
        elif scope["type"] == "websocket":
            await websocket_application(scope, receive, send)
            return
        else:
            raise NotImplementedError(f"Unknown scope type {scope['type']}")
    return asgi

async def websocket_application(scope, receive, send):
    # scopeに任意のket:valueを追加可能
    scope['room'] = 'test'
    while True:
        event = await receive()
        # debug
        print("----websocket.py----")
        print(event)
        print("scope/['room']:", scope['room'])

        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept',
            })

        if event['type'] == 'websocket.disconnect':
            break

        if event['type'] == 'websocket.receive':
            await send({
                'type': 'websocket.send',
                'text': event['text']
            })