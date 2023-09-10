import re
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth import *
from django.views.generic import ListView, FormView, CreateView
from jpd_app.models import *
from jpd_app.forms import *

# Create your views here.
# def home(request):
#     return render(request, 'home.html', )

# def products(request):
#     return render(request, 'productMenu.html', {})

# def vendors(request):
#     return render(request, 'vendorMenu.html', {})

# def contact(request):
#     return render(request, 'contact.html', {})

# def about(request):
#     return render(request, 'about.html', {})

# def photos(request):
#     return render(request, 'photos.html', {})