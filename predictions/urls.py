from django.urls import path
from . import views

urlpatterns = [
    path('', views.lore, name='lore'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('broker_register',views.broker_register,name='broker_register'),
    path('customer_register',views.customer_register,name='customer_register'),
    path('customer',views.customer,name='customer'),
    path('broker',views.broker,name='broker'),
    path('main',views.main,name='main'),
    path('estimate_price',views.estimate_price,name='estimate_price'),
    path('compose',views.compose,name='compose'),
    path('sent',views.sent,name='sent'),
    path('receive',views.receive,name='receive'),
]