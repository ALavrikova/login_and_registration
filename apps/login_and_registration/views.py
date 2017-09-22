# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
	return render (request, 'login_and_registration/index.html')

def add_user(request):
	# if request.method=='POST':
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect ('/')	
		else:
			hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
			# first_name = request.POST['first_name']
			# last_name = request.POST['last_name']
			user = User.objects.create(first_name=request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'], password = hash1)
			user.save()

			return redirect ('/success')

def login(request):
	if request.method=='POST':
		user = User.objects.filter(email = request.POST['email'])
		if len(user)==0:
			errors={}
			errors['no_email'] = "Email is not in database"
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect('/')
		else:
			hashed_password = user[0].password
			if bcrypt.checkpw(request.POST['password'].encode(), hashed_password.encode()):
				return redirect('/success')
			else: 
				errors={}
				errors['no_password_match'] = "Incorrect password"
				for tag, error in errors.iteritems():
					messages.error(request, error, extra_tags=tag)
				return redirect('/')			

	return render(request, 'login_and_registration/success.html')		

def success(request):
	return render (request, 'login_and_registration/success.html')	
