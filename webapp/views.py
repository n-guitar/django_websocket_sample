from django.shortcuts import render
from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'


async def websocket_view(socket):
    await socket.accept()
    await socket.send