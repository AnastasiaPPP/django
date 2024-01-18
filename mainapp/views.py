from django.http import HttpResponse
from django.shortcuts import render

from mainapp.models import Client


# Create your views here.




def index_page(request):
    text_i = '<h1>Главная<h1> <br> <p>всякий текст, много текста по заданию о сайте</p>'
    return HttpResponse(text_i)


def about_page(request):
    text_a = '<h1>О нас<h1> <br> <p>всякий текст, много текста по заданию о нас</p>'
    return HttpResponse(text_a)


def get_clients(request):
    client = Client.objects.all()
    response = '<br>'.join([str(client) for client in client])
    return HttpResponse(response)