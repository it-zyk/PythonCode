from django.shortcuts import render, redirect
from booktest.models import BookInfo, AreaInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
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
    # 重定向
    return HttpResponseRedirect('/index')


def delete(request, bid):
    book = BookInfo.objects.get(id=bid)
    # book.is_delete = True
    # book.save()
    book.delete()
    return redirect('/index')


def area(request):
    '''获取广州的上级地区和下级地区'''
    # 1. 获取广州市的信息
    area = AreaInfo.objects.get(atitle='广州市')
    # 2. 查询广州市的上级地区
    aParent = area.aParent
    # 3. 查询广州市的下级地区
    children = area.areainfo_set.all()
    return render(request, 'booktest/area.html', {"area": area, "parent": aParent,"children": children})
