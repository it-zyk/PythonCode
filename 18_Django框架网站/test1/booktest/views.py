from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


# http://localhost:8000/index
def index(request):
    #进行处理， 和M和T进行交互
    return HttpResponse('老铁没毛病')



