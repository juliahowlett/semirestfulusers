from django.db import models
from datetime import date

class dojos(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	desc = models.TextField
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True) 
	
	def __str__(self):
	#return "%s %s" % (self.first_name, self.last_name)
		return "{} {} {} {}" % (self.name, self.city, self.state, self.desc)
	
	
class ninjas(models.Model):
	dojo = models.ForeignKey(dojos, null = True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return "{} {}" % (self.first_name, self.last_name)
	