from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),

    #----------------------------banner-----------------------------------
    path('banner-list/', views.list_banner, name='banner_list'),
    path('banner-create/', views.create_banner, name='banner_create'),
    path('banner-detail/<int:id>/', views.detail_banner, name='banner_detail'),
    path('banner-edit/<int:id>/', views.edit_banner, name='banner_edit'),
    path('banner-delete/<int:id>/', views.delete_banner, name='banner_delete'),
    # ------------------------service----------------------------
    path('service-list/', views.list_service, name='service_list'),
    path('service-create/', views.create_service, name='service_create'),
    path('service-detail/<int:id>/', views.detail_service, name='service_detail'),
    path('service-edit/<int:id>/', views.edit_service, name='service_edit'),
    path('service-delete/<int:id>/', views.delete_service, name='service_delete'),
    #-----------------------price---------------------------------------
    path('price-list/', views.list_price, name='price_list'),
    path('price-create/', views.create_price, name='price_create'),
    path('price-detail/<int:id>/', views.detail_price, name='price_detail'),
    path('price-edit/<int:id>/', views.edit_price, name='price_edit'),
    path('price-delete/<int:id>/', views.delete_price, name='price_delete'),
    #--------------------------------about-------------------------------
    path('about-list/', views.list_about, name='about_list'),
    path('about-create/', views.create_about, name='about_create'),
    path('about-detail/<int:id>/', views.detail_about, name='about_detail'),
    path('about-edit/<int:id>/', views.edit_about, name='about_edit'),
    path('about-delete/<int:id>/', views.delete_about, name='about_delete'),
    #---------------------------------contact--------------------------------------
    path('contact-list/', views.list_contact, name='contact_list'),
    path ('contact-detail/<int:id>/', views.detail_contact, name='contact_detail'),
    path('contact-edit/<int:id>/', views.edit_contact, name='contact_edit'),
    # -----------------register, login, logout-------------------------------
    path('register/', views.register, name='register'),
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),
    # ----------------search--------------
    path('q', views.query, name='query')
]