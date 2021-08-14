from django.shortcuts import render
from Productos.models import Producto
from Cart.cart import Cart

def home(request):
    cart = Cart(request)
    product_main = Producto.objects.all()[0:3]
    product_secondary = Producto.objects.all()[3:10]
    context = {'product_main':product_main, 'product_secondary':product_secondary}
    return render(request,'home.html', context)