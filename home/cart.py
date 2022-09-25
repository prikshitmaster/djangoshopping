from django.shortcuts import render,HttpResponse


def cart(request):
    return render(request, 'cart.html')

