from django.shortcuts import render, redirect
from Productos.models import Producto
from django.contrib.auth.decorators import  login_required
from .cart import  Cart

def cart(request):
    return render(request,'Cart.html')


@login_required(login_url="login")
def add_product(request,pk):
    cart = Cart(request)
    product = Producto.objects.get( id = pk)
    cart.add(product = product)
    return redirect('cart')


@login_required(login_url="login")
def remove_product(request,pk):
    cart = Cart(request)
    product = Producto.objects.get( id = pk)
    cart.remove(product = product)
    return redirect('cart')


@login_required(login_url="login")
def decrement_product(request,pk):
    cart = Cart(request)
    product = Producto.objects.get( id = pk)
    cart.decrement(product = product)
    return redirect('cart')

@login_required(login_url="login")
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')