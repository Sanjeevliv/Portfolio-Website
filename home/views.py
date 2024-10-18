from django.shortcuts import render
from django.http import HttpResponse

def HomePageView(response):
    return HttpResponse('Hello World')
