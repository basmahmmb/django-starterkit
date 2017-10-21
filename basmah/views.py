from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json


# Create your views here.
from django.http import HttpResponse


@login_required
def index(request):
    return HttpResponse("This is my first app")
