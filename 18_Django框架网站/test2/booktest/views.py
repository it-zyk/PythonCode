from django.shortcuts import render
from booktest.models import BookInfo
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def index(request):
    '''显示图书信息'''
    # 1. 查询所有图书信息
    books = BookInfo.objects.all()
    # 2 使用模板
    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    '''新增信息'''
    b = BookInfo()
    b.btitle = '新流星蝴蝶剑'
    b.bpub_date = date(1990, 1, 1)
    b.save()
    # 让浏览器再访问首页
    # return HttpResponse('OK')
    return HttpResponseRedirect('/index')
