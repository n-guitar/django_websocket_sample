class WebSocket:
    def __init__(self, scope, receive, send):
        self._scope = scope
        self._receive = receive
        self._send = send

    def headers(self):
        return self._scope['headers']

    def path(self):
        return self._scope['path']

    def scope(self):
        return self._scope['scope']

    # receiveして、clientにwebsocket.acceptを送ってあげる
    async def accept(self):
        if self._scope['type'] == 'websocket.connect':
            await self.receive()
        await self.send({
            'type': 'websocket.accept',
        })

    async def receive(self):
        message = await self._receive()
        return message

    async def send(self, message):
        await self._send(message)

    async def send_text(self, text: str):
        await self.send({
            'type': 'websocket.send',
            "text": text
        })

    async def receive_text(self):
        print("receive_text")
        print(self)
        message = await self.receive()
        print(message)
        # return message["bytes"]
        return message