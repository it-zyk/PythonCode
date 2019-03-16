from django.shortcuts import render, redirect
from booktest.models import BookInfo, AreaInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    '''显示图书信息'''
    # 1. 查询所有图书信息
    # books = BookInfo.objects.all()
    # 2 使用模板
    # return render(request, 'booktest/index.html', {'books': books})
    return render(request, 'booktest/index.html')
