from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('loginpage',views.loginpage),
    path('registpage',views.registpage)
]