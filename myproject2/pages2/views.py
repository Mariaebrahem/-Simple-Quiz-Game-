from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("hello,world." )
    return render(request,'pages2/index.html')

def about(request):
   return render(request,'pages2/about.html')