from django.shortcuts import render

from . import models


def index(request):
    baner = models.Banner.objects.last()
    about = models.AboutUs.objects.last()
    services = models.Service.objects.all()

    prices_list = []

    for price in models.Price.objects.all().order_by('price'):
        price.body = price.body.split(',')
        prices_list.append(price)

    context = {
        'baner':baner,
        'about':about,
        'services':services,
        'prices':prices_list
    }
    return render(request, 'front/index.html', context)

def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'front/contact.html')

def service(request):
    services = models.Service.objects.all()

    context = {
        'services':services,    }
    return render(request, 'front/service.html', context)

def about(request):
    about = models.AboutUs.objects.last()

    context = {
        'about':about,
    }
    return render(request, 'front/about.html', context)

def price(request):
    prices_list = []

    for price in models.Price.objects.all().order_by('price'):
        price.body = price.body.split(',')
        prices_list.append(price)

    context = {
        'prices':prices_list,
    }
    return render(request, 'front/price.html', context)


