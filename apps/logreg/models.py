# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt
import time


# Create your models here.
class UsersManager(models.Manager):
    def users_valid(self, postData):
        errors = {}
        if postData['pw'] != postData['confpw']:
            errors['pw'] = "Password must match Confirmation"
        if not re.match("^[A-Za-z]*$",postData['name']):
            errors['name'] = "First name can only contain letters"
        if len(postData['name']) < 3:
            errors['name'] = "First name must be longer than 2 characters"
        if len(postData['username']) < 3:
            errors['username'] = "Username must be longer than 2 characters"
        try: 
            trying = Users.objects.get(username=postData['username'])
            errors['username'] = "Username already in use"
        except Users.DoesNotExist:
            pass
        return errors


    def login_valid(self, postData):
        em = postData['username']
        paw = postData['pw']
        
        errors = {}
        # Tests if username exists
        try:
            trying = Users.objects.get(username=postData['username'])
        except Users.DoesNotExist:
            errors['username'] = "Username password combo does not exist"
            return errors

        # Tests if password of that username matches password given
        a = Users.objects.get(username=em).pw 
        if bcrypt.checkpw(paw.encode(), a.encode()):
            pass
        else:
            errors['password'] = "Username password combo does not exist"
        return errors

    # def edit_user(self, postData):
    #     errors = {}
    #     if not re.match("^[A-Za-z]*$",postData['fname']):
    #         errors['fname'] = "First name can only contain letters"
    #     if not re.match("^[A-Za-z]*$",postData['lname']):
    #         errors['lname'] = "Last name can only contain letters"
    #     em = Users.objects.get(id=postData['idt']).email
    #     # Check if the email has changed in the form from what it is
    #     if postData['email'] != em:
    #         try: 
    #             trying = Users.objects.get(email=postData['email'])
    #             errors['email'] = "Email already in use"
    #         except Users.DoesNotExist:
    #             pass
        
    #     return errors
        
    # def edit_pw(self, postData):
    #     errors = {}
    #     if postData['new_pw'] != postData['pw_conf']:
    #         errors['new_pw'] = "Password must match Confirmation"
    #     return errors


class Users(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    
    pw = models.CharField(max_length=50)
    
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()

class TravelsManager(models.Manager):
    def add_valid(self, d):
        errors={}


        if d['traveldate_from_year'] > d['traveldate_to_year']:
            errors['travel_date_from'] = "Travel date to must not be before travel date from"

        elif d['traveldate_from_year'] == d['traveldate_to_year'] and d['traveldate_from_month'] > d['traveldate_to_month']:
            errors['travel_date_from'] = "Travel date to must not be before travel date from"

        elif d['traveldate_from_year'] == d['traveldate_to_year'] and d['traveldate_from_month'] == d['traveldate_to_month'] and d['traveldate_from_day'] > d['traveldate_to_day']:
            errors['travel_date_from'] = "Travel date to must not be before travel date from"

        if int(time.strftime('%Y')) > int(d['traveldate_from_year']):
            errors['travel_date_from'] = "Travel date from must be in the future"
            print "Year"

        elif int(time.strftime('%Y')) == int(d['traveldate_from_year']) and int(time.strftime('%m')) > int(d['traveldate_from_month']):
            errors['travel_date_from'] = "Travel date from must be in the future"
            print "Month"
        
        elif (int(time.strftime('%Y')) == int(d['traveldate_from_year'])) and (int(time.strftime('%m')) == int(d['traveldate_from_month'])) and (int(time.strftime('%d')) > int(d['traveldate_from_day'])):
            errors['travel_date_from'] = "Travel date from must be in the future"
            print "Day"

        return errors

        

class Travels(models.Model):
    destination = models.CharField(max_length= 100)
    description = models.CharField(max_length=100)
    traveldate_from = models.CharField(max_length=50)
    traveldate_to = models.CharField(max_length=50)
    users = models.ManyToManyField(Users, related_name="travels")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TravelsManager()