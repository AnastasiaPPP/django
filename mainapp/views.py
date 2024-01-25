from django.http import HttpResponse
from django.shortcuts import render
from datetime import timedelta, datetime
from itertools import chain

from mainapp.models import Client, Order, Good


# Create your views here.


def index_page(request):
    text_i = '<h1>Главная<h1> <br> <p>всякий текст, много текста по заданию о сайте</p>'
    return HttpResponse(text_i)


def about_page(request):
    text_a = '<h1>О нас<h1> <br> <p>всякий текст, много текста по заданию о нас</p>'
    return HttpResponse(text_a)


def get_orders(request, days):
    now = datetime.today() - timedelta(days=days)
    orders = Order.objects.filter(date__gte=now)
    return render(request, 'mainapp/sorted_orders.html', {'orders': orders})


def get_clients(request):
    client = Client.objects.all()
    response = '<br>'.join([str(client) for client in client])
    return HttpResponse(response)


def get_client_orders(request, pk):
    orders = Order.objects.filter(client_id=pk)
    li = [order.get_goods() for order in orders]
    sorted_list = list(chain.from_iterable(li))
    return render(request, 'mainapp/orders_goods.html', {'orders': orders, 'goods': sorted_list})
