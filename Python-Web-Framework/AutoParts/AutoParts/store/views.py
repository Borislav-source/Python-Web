import json

from django.http import JsonResponse
from django.shortcuts import render

from AutoParts.accounts.models import Profile
from AutoParts.parts.models import Product
from AutoParts.store.models import Order, OrderItem


def cart(request):
    customer = Profile.objects.get(user=request.user)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = Profile.objects.get(user=request.user)
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added successfully', safe=False)


def checkout(request):
    customer = Profile.objects.get(user=request.user)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order)
    context = {
        'orderItem': orderItem,
        'order': order,
    }
    return render(request, 'store/checkout.html', context)
