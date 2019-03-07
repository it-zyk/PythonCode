from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')

# request 包含浏览器的信息，num 参数信息


def show_arg(request, num):
    return HttpResponse(num)


def login(request):
    return render(request, 'booktest/login.html')
