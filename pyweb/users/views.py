from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def html(request):
    return HttpResponse("userIndex")