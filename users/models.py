from django.db import models
#from django.contrib import messages
		
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email_address = models.EmailField(max_length=254)
	age_of = models.IntegerField(default=0)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
