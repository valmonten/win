# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
import bcrypt
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Create your views here.
# def home(request):
#     return render(request, 'logreg/home.html')

def show(request):
    if not request.session.get('path'):
        request.session['path'] = "Log"
    context = {
        "form": Sign_in_forms,
        "formy": Register_forms,
        "path": request.session['path']
    }
    return render(request, 'logreg/collected.html', context)

def show_reg(request):
    context = {
        "form": Sign_in_forms,
        "formy": Register_forms,
        
    }
    return render(request, 'logreg/home.html', context)

def sign_in(request):
    request.session['path'] = "Log"
    errors = Users.objects.login_valid(request.POST)
    em = request.POST['username']
    if len(errors):
        
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect ('/')
    request.session['log_id'] = Users.objects.get(username=em).id
    request.session['name'] = Users.objects.get(username=em).name
    
    
    return redirect('/travels')



def register(request):
    request.session['path']= "Reg"
    errors = Users.objects.users_valid(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())

        Users.objects.create(name=request.POST['name'], username=request.POST['username'], pw=hash1)
        
        request.session['name'] = request.POST['name']
        em = request.POST['username']
        
        abc = Users.objects.get(username=em).id
        request.session['log_id'] = abc

    return redirect('/travels')

def logout(request):
    request.session.clear()
    return redirect('/')
