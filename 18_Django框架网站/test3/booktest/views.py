from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')


def show_arg(request, num):
    return HttpResponse(num)
