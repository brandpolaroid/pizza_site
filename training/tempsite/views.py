from django.shortcuts import render, redirect
from .models import Pizza, Order, Offered
from .forms import AddOrder
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from json import load, dumps
import datetime


def home(request):
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    if all(Order.objects.all()[i].user_ip != ip for i in range(len(Order.objects.all()))):
        user_cart = Order.objects.create(user_ip=ip, product_id={}, price=0)
    else:
        user_cart = Order.objects.get(user_ip=ip)

    if request.method == "POST":
        user_request = load(request)
        if user_request['operation'] == 1:
            pizza_id = user_request['selected-pizza']
            amount_pizza_id = user_cart.product_id.get(pizza_id, 0)
            amount_to_add = user_request['amount']
            user_cart.product_id[pizza_id] = int(min(amount_pizza_id + amount_to_add, 20))
            user_cart.save()
            return HttpResponse(user_cart.product_id.get(pizza_id))

        elif user_request['operation'] == 0:
            pizza_id = user_request['selected-pizza']
            user_cart.product_id[pizza_id] = 0
            user_cart.save()
            return HttpResponse(1)

        elif user_request['operation'] == 2:
            answer_amount = dumps(user_cart.product_id)
            return HttpResponse(answer_amount)

    pizzas = Pizza.objects.order_by('id')
    data = {'images': pizzas, 'user-cart': user_cart}
    return render(request, 'tempsite/home.html', data)


def cart(request):
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    if all(Order.objects.all()[i].user_ip != ip for i in range(len(Order.objects.all()))) or Order.objects.all() is None:
        user_cart = Order.objects.create(user_ip=ip, product_id={}, status=False)
    else:
        user_cart = Order.objects.get(user_ip=ip)
    form = AddOrder(request.POST or None)
    if request.method == "POST":
        if request.POST.get('phone', 0) != 0:
            if form.is_valid():
                pizzas = Pizza.objects
                name = form.cleaned_data.get('name')
                phone = form.cleaned_data.get('phone')
                address = form.cleaned_data.get('address')
                price = 0
                products = {}
                for k, v in user_cart.product_id.items():
                    price += v * pizzas.get(id=k).price
                    if v != 0:
                        products.update({pizzas.get(id=k).name: v})
                if len(products) == 0:
                    return render(request, 'tempsite/cart_offer.html', {'result': 'Заказ не принят в обработку, нужно выбрать товар!'})

                new_order = Offered.objects.create(user_name=name,
                                                   user_phone=phone,
                                                   user_address=address,
                                                   product_id=products,
                                                   date_time_start=datetime.datetime.now(),
                                                   order_price=price,
                                                   status=0)
                user_cart.delete()
                return render(request, 'tempsite/cart_offer.html', {'result': 'Заказ принят в обработку!'})
        else:
            return home(request)

    pizzas = Pizza.objects.order_by('id')
    users_pizzas = []
    form = AddOrder
    total_price = 0
    for i in user_cart.product_id:
        if user_cart.product_id[i] != 0:
            users_pizzas.append(pizzas.get(id=i))
            total_price += pizzas.get(id=i).price * user_cart.product_id[i]
    data = {"users_pizzas": users_pizzas, "form": form, "price": total_price}
    return render(request, 'tempsite/cart.html', data)


def cart_offer(request):
    return render(request, 'tempsite/cart_offer.html')


@login_required()
def orders(request):
    all_orders = Offered.objects.order_by('status', '-date_time_stop', '-date_time_start')
    pizzas = Pizza.objects.all()

    all_data = []
    if request.method == "POST":
        id_to_switch = load(request)['id']
        order_to_switch = Offered.objects.get(id=id_to_switch)
        if order_to_switch.status == 0:
            order_to_switch.status = 1
            order_to_switch.date_time_stop = datetime.datetime.now()
        elif order_to_switch.status == 1:
            order_to_switch.status = 0
            order_to_switch.date_time_stop = None
        order_to_switch.save()

    for i, e in enumerate(all_orders):
        data = []
        data.append(i + 1)
        data.append(e.id)
        data.append(e.user_name)
        data.append(e.user_phone)
        data.append(e.user_address)
        data.append(e.date_time_start)
        data.append(e.date_time_stop)
        data.append(e.order_price)
        data.append(e.product_id)
        if e.status == 0:
            data.append("Готовится")
        elif e.status == 1:
            data.append("Готов")
        all_data.append(data)
    to_page = {'data': all_data}
    return render(request, 'tempsite/orders.html', to_page)
