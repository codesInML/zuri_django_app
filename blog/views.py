from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return HttpResponse('<h1>Blog Home, Zuri App</h1>')


def about(req):
    return HttpResponse('<h1>Blog About</h1>')