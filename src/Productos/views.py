from django.shortcuts import render,redirect
from .forms import ProductoForm
from .models import Producto
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.


@staff_member_required
def agregar_producto(request):
    form = ProductoForm()
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            imagen = form.cleaned_data['imagen']
            return redirect('home')
        else:
            print(form.errors)
            raise Http404 
    context = {'form':form}
    return render(request,'agregar_producto.html',context)

def show_product(request,pk):
    prd = Producto.objects.get(id=pk)
    context = {'prd':prd}
    return render(request,'show_product.html',context)

@staff_member_required
def editar_producto(request, pk):
    
    tarea = Producto.objects.get(id=pk)
    form = ProductoForm(instance = tarea)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance = tarea)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form, 'tarea':tarea}
    return render(request,'editar_producto.html',context)

@staff_member_required
def borrar_producto(request,pk):
    prd = Producto.objects.get(id=pk)
    if request.method == 'POST':
        prd.delete()
        return redirect('home')

    context = {'prd':prd}
    return render(request,'borrar_producto.html',context)


def search(request):
    if request.method == "POST":
        busqueda = request.POST['busqueda']
        title_producto = Producto.objects.filter(title__contains = busqueda)
        description_producto = Producto.objects.filter(description__contains=busqueda)
        context ={
            'busqueda':busqueda,
            'title_producto':title_producto,
            'description_producto':description_producto,
            }
        return render(request,'search.html',context)
    else:
        context={}
        return render(request,'search.html',context)

def search_categoria(request):
    if request.method == "POST":
        busqueda = request.POST['busqueda']
        category_producto = Producto.objects.filter(category__contains=busqueda)
        context = {'busqueda':busqueda,'category_producto':category_producto}
        return render(request,'search.html',context)
    else:
        context={}
        return render(request,'search.html',context)
