# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def basic_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 1:
			errors["first_name"] = 'First name should be more than 1 character!'
		elif len(postData['last_name']) < 1:
			errors["last_name"] = 'Last name should be longer than 1 character!'  
		elif len(postData['email'])<1:
			errors["email"] = 'Email length should be longer than 1 character!'	
		elif not EMAIL_REGEX.match(postData['email']):
			errors["email"] = 'Invalid email format!'		  
		elif len(postData['password'])<1:
			errors["password"] = 'Password length should be longer than 1 character!'	
		elif postData['password']!=postData['verify_password']:
			errors["not_password_match"] = 'Password is incorrect!' 
		return errors;

class User(models.Model):
	id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	objects=UserManager();  


