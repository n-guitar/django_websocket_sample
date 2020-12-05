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