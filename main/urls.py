from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name = "index"),
    path('', views.home, name = "home"),
    path('create', views.create, name = "create"),
    path('view/', views.view, name = "view")
    # example -> was testing before
    # path('<str:name>', views.index, name = "index")
    
]