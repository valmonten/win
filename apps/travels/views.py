# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..logreg.models import *
from .forms import *
import time
from django.contrib import messages

# Create your views here.
def dashboard(request):
    if not request.session.get('log_id'):
        return redirect('/')
    
    user = Users.objects.get(id=request.session['log_id'])
    n = Travels.objects.exclude(users=user)
    m = Travels.objects.filter(users=user)


    
    context ={
        'travels2':n,
        'travels':m,
        'son':user,
    }
    return render(request, 'travels/dashboard.html', context)

def add(request):
    if not request.session.get('log_id'):
        return redirect('/')
    context ={
        'form':Travel
    }
    return render(request, 'travels/add.html', context)

def adding(request):
    errors = Travels.objects.add_valid(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/travels/add')
    tfrom = str(request.POST['traveldate_from_month'])+"-"+str(request.POST['traveldate_from_day'])+'-'+str(request.POST['traveldate_from_year'])
    tto = str(request.POST['traveldate_to_month'])+"-"+str(request.POST['traveldate_to_day'])+'-'+str(request.POST['traveldate_to_year'])
    Travels.objects.create(destination=request.POST['destination'], description=request.POST['description'], traveldate_from=tfrom, traveldate_to=tto)
    b = Travels.objects.order_by('-created_at')[0]
    c = Users.objects.get(id=request.session['log_id'])
    b.users.add(c)
    

    
    return redirect('/travels')

def destination(request, name):
    win = Travels.objects.get(id=name)
    names = Travels.objects.get(id=name).users.exclude(name=request.session['name'])
    context ={
        "name":win,
        "yup":names,
    }
    return render(request, 'travels/destination.html', context)

def join(request, name):
    f = Travels.objects.get(id=name)
    c = Users.objects.get(id=request.session['log_id'])
    f.users.add(c)
    return redirect('/travels')
    

