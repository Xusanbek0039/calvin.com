
from django.shortcuts import render
from django.views.generic import TemplateView



# TemplateView bu teplatesni korsat degani name esa htmlga yoldur 
class HomePageView(TemplateView):
    template_name = 'boshmenu.html'


class HaqidaView(TemplateView):
    template_name = 'haqida.html'


class TestView(TemplateView):
    template_name = 'test.html'