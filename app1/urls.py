from . import views
from .models import *
from django.shortcuts import redirect,render
from django.urls import path

urlpatterns = [

   path("", views.index, name="index"),
    path("companyprofile/<int:id>/<int:pk>", views.companyprofile, name="companyprofile"),
     path("about-us", views.about, name="about-us"),
      path("add_category", views.add_category, name="add_category"),

       path("adding_category", views.adding_category, name="adding_category"),

       path("add_company", views.add_company, name="add_company"),

        path("adding_company", views.adding_company, name="adding_company"),


      path("adminpanel", views.adminpanel, name="adminpanel"),
     path("category/<int:id>", views.category, name="category"),    
    path("blog-list-4", views.blog, name="blog-list-4"),
    path("all_companies", views.all_companies, name="all_companies"),
    
]
