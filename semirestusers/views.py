from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Users

def index(request): #show
	print(Users.objects.all())	
	context = {
	'allusers' : Users.objects.all()
	}
	return render(request, 'semirestusers/index.html', context)

def show(request, user_id): #GET /users/<id> 
	print(user_id)
	context = {
	'the_user' : Users.objects.get(id=user_id)
	}
	return render(request, 'semirestusers/show.html', context)	
	

def new(request):  #/users/new
	return render(request, 'semirestusers/new.html')
	
def create(request):  #/users/create	
	print(request.POST)	
	#Users.objects.add(request.POST)
	errors = Users.objects.validate_registration(request.POST)	
	
	if errors:
		print("errors from views", errors)
		#messages.add_message(request, messages.INFO, 'Errors in the entry.')
		for fail in errors:
			messages.error(request, fail)
		return redirect('/new')
		
	print ("success!")	
	return redirect('/index')
   
def update(request, user_id): #GET /edit/<id> 
	print(user_id)
	context = {
	'the_user' : Users.objects.get(id=user_id)
	}
	return redirect(request, '/create', context)		
   
def destroy(request, user_id): #GET /users/<id>/destroy   
	print("data = ", user_id)
	Users.objects.get(id=user_id).delete()
	return redirect('/index')
 
   