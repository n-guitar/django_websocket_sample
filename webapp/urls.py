from django.urls import path
from .views import IndexView, AsuncIndex

urlpatterns = [
    path('', IndexView.as_view() , name='IndexView' ),
    path('async/', AsuncIndex, name='AsyncIndex' ),
]