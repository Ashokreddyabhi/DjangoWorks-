from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobs_info(request):
    s = '<h1>hyd jobs info</h1>'
    return HttpResponse(s)
def bengulurjobs_info(request):
    s = '<h1>bengulur jobs info</h1>'
    return HttpResponse(s)
def chennaijobs_info(request):
    s = '<h1>chennai jobs info</h1>'
    return HttpResponse(s)
    