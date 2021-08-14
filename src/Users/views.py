from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.


def registro(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            redirect('home')
    context = {'form': form}
    return render(request,'register.html',context)
