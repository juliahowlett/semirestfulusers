#from __future__ import unicode_literals
from datetime import date
from django.db import models
import re

#EMAIL_MATCH = re.compile(r'^a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$')

class UserManager(models.Manager):

	def add(self, post_data):
		self.create(
			first_name = post_data['first_name'],
			last_name = post_data['last_name'],
			email = post_data['email']
			)
		print(post_data)

	def validate_registration(self, post_data):
		print(post_data) 
	
		errors = []
		#check all fields for input - loop through entire dictionary looking for a single empty field
		for  key, value in post_data.items():
			if len(value) < 1:
				errors.append("All fields are required")
				print(errors)
				break

		#min length for name
		if len(post_data['first_name']) < 3 or len(post_data['last_name']) < 3:
			errors.append("all fields must be at least 3 character") 
			print(errors)
		#email check
		#if not re.match(EMAIL_MATCH, post_data['email']):
			#errors.append("email not valid")
			#print(errors)
		#Existing email - this will return [] if no match is found
		if self.filter(email=post_data['email']):
			errors.append("email in use")	
			print(errors)
		return errors
		
		#if no errors, create a User
		if not errors:
			self.create(
				first_name = post_data['first_name'],
				last_name = post_data['last_name'],
				email = post_data['email']
				)
			
class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	
	objects = UserManager()
	
	def __repr__(self):
		return "<fullname {} {}, email {}, created {}>".format(self.first_name,self.last_name,self.email, self.created_at)	
		
		

		
#from apps.semirestusers.models import *		
#Users.objects.create(first_name="Peewee", last_name="Herman", email="pewee@gmail.com")
#Users.objects.create(first_name="Miss", last_name="Yvonne", email="myvonne@gmail.com")	
#for user in Users.all(): print Users