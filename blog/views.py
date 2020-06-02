from django.shortcuts import render, HttpResponse
from blog import models

# Create your views here.
def index(request):

    return HttpResponse("OK")