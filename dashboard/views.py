from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main import models
from django.contrib import messages
from django.db.models import Q

@login_required(login_url='dashboard:log_in')
def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()
    data_1 = [1,2,3,4,5,6,7]
    data_2 = [2,3,4,5,6,7,8]
    context = {
        'contacts':contacts,

        'data_1':data_1,
        'data_2':data_2,
    }
    return render(request, 'dashboard/index.html', context)



@login_required(login_url='dashboard:log_in')
def create_banner(request):
    if request.method == "POST":
        try:
            title = request.POST['title']
            body = request.POST['body']
            models.Banner.objects.create(
                title=title,
                body=body,
            )
            messages.success(request, 'Banner muvaffaqiyatli yaratilindi')
        except:
            messages.error(request, 'Banner yaratilishda xatolik')


    return render(request, 'dashboard/banner/create.html')


@login_required(login_url='dashboard:log_in')
def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)

def detail_banner(request, id):
    banner = models.Banner.objects.get(id=id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_banner(request, id):
    banner = models.Banner.objects.get(id=id)
    if request.method =='POST':
        try:
            banner.title = request.POST['title']
            banner.body = request.POST['body']
            banner.save()
            messages.success(request, 'Banner muvaffaqiyatli o`zgartirildi')
        except:
            messages.error(request, 'Banner o`zgartirishda xatolik')
        return redirect('dashboard:banner_detail', banner.id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/edit.html', context)

def delete_banner(request, id):
    try:
        models.Banner.objects.get(id=id).delete()
        messages.error(request, 'Banner o`chirildi')
    except:
        messages.error(request, 'Banner o`chirishda xatolik')
    return redirect('dashboard:banner_list')



@login_required(login_url='dashboard:log_in')
def create_service(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            body = request.POST['body']
            icon = request.POST['icon']
            models.Service.objects.create(
                name=name,
                body=body,
                icon=icon
            )
            messages.success(request, 'Servis muvaffaqqiyatli yaratildi')
        except:
            messages.error(request, 'Servis yaratishda xatolik')
    return render(request, 'dashboard/service/create.html')


@login_required(login_url='dashboard:log_in')
def list_service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'dashboard/service/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_service(request, id):
    service = models.Service.objects.get(id=id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_service(request, id):
    service = models.Service.objects.get(id=id)
    if request.method =='POST':
        try:
            service.name = request.POST['name']
            service.body = request.POST['body']
            service.icon = request.POST['icon']
            service.save()
            messages.success(request, 'Servis muvaffaqqiyatli o`zgartirildi')
        except:
            messages.error(request, 'Servis o`zgartirishda xatolik')

        return redirect('dashboard:service_list', service.id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/edit.html', context)


@login_required(login_url='dashboard:log_in')
def delete_service(request, id):
    try:
        models.Service.objects.get(id=id).delete()
        messages.error(request, 'Servis muvaffaqqiyatli o`chirildi')
    except:
        messages.error(request, 'Servis o`chirishda xatolik')
    return redirect('dashboard:service_list')


@login_required(login_url='dashboard:log_in')
def create_price(request):
    if request.method == "POST":
        try:
            title = request.POST['title']
            price = request.POST['price']
            body = request.POST['body']
            models.Price.objects.create(
                title=title,
                price=price,
                body=body
            )
            messages.success(request, 'Price muvaffaqqiyatli yaratildi.')
        except:
            messages.error(request, 'Price yaratishda xatolik')
    return render(request, 'dashboard/price/create.html')


@login_required(login_url='dashboard:log_in')
def list_price(request):
    prices = models.Price.objects.all()
    context = {
        'prices':prices
    }
    return render(request, 'dashboard/price/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_price(request, id):
    prices = models.Price.objects.get(id=id)
    context = {
        'prices':prices
    }
    return render(request, 'dashboard/price/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_price(request, id):
    price = models.Price.objects.get(id=id)
    if request.method =='POST':
        try:
            price.title = request.POST['title']
            price.price = request.POST['price']
            price.body = request.POST['body']
            price.save()
            messages.success(request, 'Price muvaffaqqqiyatli o`zgartirildi')
        except:
            messages.error(request, 'Price o`zgartirishda xatolik')
        return redirect('dashboard:price_list')
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/edit.html', context)


@login_required(login_url='dashboard:log_in')
def delete_price(request, id):
    try:
        models.Price.objects.get(id=id).delete()
        messages.error(request, 'Price muvaffaqqiyatli o`chirildi')
    except:
        messages.error(request, 'Price o`chirishda xatolik')
    return redirect('dashboard:price_list')


@login_required(login_url='dashboard:log_in')
def create_about(request):
    if request.method == "POST":
        try:
            body = request.POST['body']
            models.AboutUs.objects.create(
                body=body
            )
            messages.success(request, 'About Us muvaffaqqiyatli yaratildi')
        except:
            messages.error(request, 'About Us yaratishda xatolik')
    return render(request, 'dashboard/about/create.html')


@login_required(login_url='dashboard:log_in')
def list_about(request):
    about = models.AboutUs.objects.all()
    context = {
        'about':about
    }
    return render(request, 'dashboard/about/list.html', context)

@login_required(login_url='dashboard:log_in')
def detail_about(request, id):
    about = models.AboutUs.objects.get(id=id)
    context = {
        'about':about
    }
    return render(request, 'dashboard/about/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_about(request, id):
    about = models.AboutUs.objects.get(id=id)
    if request.method =='POST':
        try:
            about.body = request.POST['body']
            about.save()
            messages.success(request, 'About Us muvaffaqqiyatli o`zgartirildi')
        except:
            messages.error(request, 'About Us o`zgartirishda xatolik')
        return redirect('dashboard:about_list')
    context = {
        'about':about
    }
    return render(request, 'dashboard/about/edit.html', context)

@login_required(login_url='dashboard:log_in')
def delete_about(request, id):
    try:
        models.AboutUs.objects.get(id=id).delete()
        messages.error(request, 'About Us muvaffaqqiyatli o`chirildi')
    except:
        messages.error(request, 'About Us o`chirishda xatolik')
    return redirect('dashboard:about_list')


@login_required(login_url='dashboard:log_in')
def list_contact(request):   
    contacts = models.Contact.objects.all()
    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/contact/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_contact(request, id):
    contacts = models.Contact.objects.get(id=id) 
    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/contact/detail.html', context)

@login_required(login_url='dashboard:log_in')
def edit_contact(request, id):
    contact = models.Contact.objects.get(id=id)
    if request.method == "POST":
        try:
            is_show = request.POST.get('is_show')  
            contact.is_show = is_show == 'on'
            contact.save()
            messages.success(request, 'Contactdagi ma`lumot muvaffaqqiyatli o`zgartirildi')
        except:
            messages.error(request, 'Ma`lumotni o`zgartirishda xatolik yuz berdi')
        return redirect('dashboard:contact_list')
    context = {
        'contact': contact, 
    }
    return render(request, 'dashboard/contact/edit.html', context)


# ------------------------------register, login, logout----------------------------
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            User.objects.create_user(
                username=username,
                password=password
            )
            return redirect('dashboard:index')
    return render(request, 'dashboard/auth/register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return render(request, 'dashboard/auth/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('main:index')


def query(request):
    q = request.GET['q']
    banners = models.Banner.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    services = models.Service.objects.filter(Q(name__icontains=q) | Q(body__icontains=q))
    price = models.Price.objects.filter(Q(title__icontains=q) | Q(body__icontains=q) | Q(price__icontains=q))
    contact = models.Contact.objects.filter(Q(name__icontains=q) | Q(email__icontains=q) | Q(phone__icontains=q))
    about = models.AboutUs.objects.filter(Q(body__icontains=q))
    context = {
        'banners':banners,
        'services':services,
        'price':price,
        'contact':contact,
        'about':about,
    }
    return render(request, 'dashboard/query.html', context)