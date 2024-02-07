from django.http import HttpResponse
from django.shortcuts import render
from datetime import timedelta, datetime
from itertools import chain

from mainapp.models import Client, Order, Good
from .forms import ImageForm, GoodForm
from django.core.files.storage import FileSystemStorage


def index_page(request):
    text_i = '<h1>Главная<h1> <br> <p>всякий текст, много текста по заданию о сайте</p>'
    return HttpResponse(text_i)


def get_orders(request, days):
    now = datetime.today() - timedelta(days=days)
    orders = Order.objects.filter(date__gte=now)
    return render(request, 'mainapp/sorted_orders.html', {'orders': orders})

def get_goods(request):
    goods = Good.objects.all()
    response = '<br>'.join([str(client) for client in goods])
    return HttpResponse(response)
def get_clients(request):
    client = Client.objects.all()
    response = '<br>'.join([str(client) for client in client])
    return HttpResponse(response)


def get_client_orders(request, pk):
    orders = Order.objects.filter(client_id=pk)
    li = [order.get_goods() for order in orders]
    sorted_list = list(chain.from_iterable(li))
    return render(request, 'mainapp/orders_goods.html', {'orders': orders, 'goods': sorted_list})


def create_good(request):
    if request.method == 'POST':
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST['name']
            price = request.POST['price']
            count = request.POST['count']
            image = form.cleaned_data['image']
            good = Good(name=name, price=price, count=count, image=image)
            good.save()
            return HttpResponse('Товар сохранен')
        print(form.errors)
        return HttpResponse('Ошибка валидации')

    else:
        form = GoodForm()
        return render(request, 'mainapp/good_form.html', {'form': form})
