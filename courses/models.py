from django.db import models
from datetime import date

#course name > 5 and description > 15

class CourseManager(models.Manager):

	def add(self, post_data):
		self.create(
			name = post_data['name'],
			desc = post_data['desc']
			)
		print(post_data)

	def validate_registration(self, post_data):
		print(post_data) 
	
		errors = []
		for  key, value in post_data.items():
			if len(value) < 1:
				errors.append("All fields are required")
				print(errors)
				break

		#min length for name
		if len(post_data['name']) < 5:
			errors.append("name must be at least 5 characters") 
			print(errors)
		#min length for course
		if len(post_data['desc']) < 15:
			errors.append("description must be at least 15 character") 
			print(errors)
			return(errors)	
		#if no errors, create Course
		if not errors:
			self.create(
				name = post_data['name'],
				desc = post_data['desc']
				)
			
class Courses(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=1000)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	
	objects = CourseManager()
	
	def __repr__(self):
		return "<name {}, desc {}, created {}>".format(self.name, self.desc, self.created_at)	
		
		

