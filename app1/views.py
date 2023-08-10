from django.contrib.auth import authenticate, login,  logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
from itertools import chain
from django.contrib import messages
import itertools
from .models import *
from django.db.models import Q
from django.db.models import Count
from django.utils import timezone
from django.db.models import Q, Count
import datetime
from django.db.models import F
from django.contrib.auth.hashers import make_password
from django.db.models import Avg
from app1.models import company


import datetime

from datetime import datetime, timedelta
import requests


from decimal import Decimal


def index(request):
    cat = categories.objects.all()  # Add parentheses to the .all() method
    return render(request, "index.html", {"cat": cat})



def companyprofile(request,id,pk):
    comp=company.objects.filter(category_name=id,id=pk)
    return render(request,"companyprofile.html",{"comp":comp} )


def about(request):
    return render(request,"about-us.html")


def add_category(request):
    return render(request,"add_category.html")



def adding_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        
        # Handle image upload
        image = request.FILES.get('image')
        
        new_category = categories(category_name=category_name, image=image)
        new_category.save()
        
        return redirect('add_category')  # Redirect to the category list page after adding a new category
    
   


from django.shortcuts import render, redirect
from .models import company

def add_company(request):

    cat=categories.objects.all()

    return render(request, 'add_company.html',{"cat":cat})


def adding_company(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        company_n = request.POST.get('company_n')
        description = request.POST.get('description')
        address = request.POST.get('address')
        company_image = request.FILES.get('company_image')
        mobile = request.POST.get('mobile')
        alt_mobile = request.POST.get('alt_mobile')
        email = request.POST.get('email')
        web_link = request.POST.get('web_link')
        fb_link = request.POST.get('fb_link')
        insta_link = request.POST.get('insta_link')
        linkdin_link = request.POST.get('linkdin_link')
        twit_link = request.POST.get('twit_link')
        service_1 = request.POST.get('service_1')
        service_2 = request.POST.get('service_2')
        service_3 = request.POST.get('service_3')
        service_4 = request.POST.get('service_4')
        image = request.FILES.get('image')
       

        new_company = company(
          
            company_n=company_n,
            description=description,
            address=address,
            company_image=company_image,
            mobile=mobile,
            alt_mobile=alt_mobile,
            email=email,
            fb_link=fb_link,
            insta_link=insta_link,
            linkdin_link=linkdin_link,
            twit_link=twit_link,
            service_1=service_1,
            service_2=service_2,
            service_3=service_3,
            service_4=service_4,
            image=image,
           
            web_link=web_link
        )
        if category_name:
            try:
                intr_instance = categories.objects.get(id=category_name)
                new_company.category_name = intr_instance
               
            except categories.DoesNotExist:
                pass     
        new_company.save()

        return redirect('add_company')  # Redirect to the company list view after successful submission

  


def add_category(request):
    return render(request,"add_category.html")



def adminpanel(request):
    return render(request,"adminpanel.html")



def blog(request):
    return render(request,"blog-list-4.html")

def all_companies(request):
    companies = company.objects.all()
    print(companies)
    return render(request, "all_companies.html", {'companies': companies})



def category(request,id):
    comp=company.objects.filter(category_name=id)
    return render(request,"category.html",{"comp":comp})

