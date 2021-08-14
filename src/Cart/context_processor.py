def cart_total_import(request):
    total = 0
    if request.user.is_authenticated:   
        for key, value in request.session['cart'].items():
            total = total + int(value['precio'])*value['quantity']
    return {'cart_total_amout':total}


    