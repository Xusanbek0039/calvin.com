from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePageView.as_view(),name='boshmenu'),
    path('haqida/',HaqidaView.as_view(),name='haqida'),
    path('test/',TestView.as_view(), name = 'test'),
    ]