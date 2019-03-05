from django.shortcuts import render
from booktest.models import BookInfo
# Create your views here.




def index(request):
    '''显示图书信息'''
    # 1. 查询所有图书信息
    books = BookInfo.objects.all()
    # 2 使用模板
    render(request,'templates/index.html', {'books':books})
