from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse

def index(request):
    return  HttpResponse("sdjkflksdjflkasdsdf")

def shiyan(request,num):
    return HttpResponse("zheshi-%s"%(num))

def new(request):
    #
    return render(request,'myapp/new1.html')
