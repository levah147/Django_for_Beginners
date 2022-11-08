from django.shortcuts import render
from django.http import HttpResponse

def homepagesview(rewuest):
    return HttpResponse('hello world!')