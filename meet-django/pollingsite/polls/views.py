from django.shortcuts import render
from django.http import HttpResponse

from models import Poll, Choice
def Hello(request): 
	return render(request, ‘template_name.html’)
# Create your views(functions) here.
# Remember each function/view the first argument/input has to be request
