from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
	response = "Hello, I am the Book Authors app!"
	return HttpResponse(response)
