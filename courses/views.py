from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Courses

def index(request): 
	print(Courses.objects.all())	
	context = {
	'allcourses' : Courses.objects.all()
	}
	return render(request, 'courses/index.html', context)
	
def create(request):  	
	print(request.POST)	
	errors = Courses.objects.validate_registration(request.POST)	
	
	if errors:
		print("errors from views", errors)
		for fail in errors:
			messages.error(request, fail)			
		return redirect('/index')
		
	print ("success!")	
	return redirect('/index')

def show(request, course_id):
	print(course_id)
	context = {
	'the_course' : Courses.objects.get(id=course_id)
	}
	return render(request, 'courses/edit.html', context)		
   	
   
def destroy(request, course_id):    
	print("data = ", course_id)
	Courses.objects.get(id=course_id).delete()
	return redirect('/index')
 
   