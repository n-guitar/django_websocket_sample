from django.urls import path
from .views import IndexView, websocket_view

# app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view() , name='IndexView' ),
    path('ws/', websocket_view, name='websocket_view' ),
]