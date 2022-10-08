from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('home/', views.home, name="home"),
    path('buy/<id>', views.buy,name= "buy"),
    path('placeOrder/', views.placeOrder,name= "placeOrder"),
]
