from datetime import date
from django.db import models

class Books(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=100)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True) 
	
	def __str__(self):
		return "{} {} {}" % (self.name, self.desc, self.author)	
	
class Authors(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=254)
	notes = models.TextField(max_length=100, null=True, default='')
	book = models.ForeignKey(Books, null=True)
	#book = models.ManytoManyField(Books, null=True, on_delete=models.CASCADE) #, related_name="id"
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return "{} {} {} {} {}" % (self.first_name, self.last_name, self.email, self.notes, self.book)
	