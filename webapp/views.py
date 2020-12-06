from django.shortcuts import render
from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'

async def websocket_view(socket):
    await socket.accept()
    await socket.send_text("socket start")

    while True:
        message = await socket.receive_text()
        await socket.send_text('hello')