from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
	response = "Hello, I am the Dojo Ninjas app!"
	return HttpResponse(response)
	
def index2(req):
	#fruit= {
	#	"fruits" : ["banana", "apple", "cherry"]
	#}
	return render(req, 'registration/index.html')

def signup(request):
	User.objects.check_it_out(request)
	return redirect('/')	