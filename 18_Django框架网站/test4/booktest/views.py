from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from booktest.models import BookInfo
# Create your views here.

# /index


def index(request):
    pass
    # 1 加载模板文件 获取模板对象
    tempt = loader.get_template('booktest/index.html')
    # 2 定义模板上下问，给模板文件传数据
    context = RequestContext(request, {})
    # 3 模板渲染， 产生一个替换后的html内容
    rest_html = tempt.render(context)
    # 返回应答
    return HttpResponse(rest_html)


def temp_var(request):
    '''模板变量'''
    my_dic = {'title': '字典类型'}
    my_list = [1, 2, 3]
    book = BookInfo.objects.get(id=1)
    # 定义模板上下文
    context = {'my_dic': my_dic, 'my_list': my_list, 'book': book}
    return render(request, 'booktest/temp_var.html', context)


def temp_tags(request):
    '''模板标签'''
    # 查找所有书目
    books = BookInfo.objects.all()
    return render(request, 'booktest/temp_tags.html', {"books": books})


def temp_filter(request):
    '''模板标签'''
    # 查找所有书目
    books = BookInfo.objects.all()
    return render(request, 'booktest/temp_filter.html', {"books": books})


def temp_inherit(request):
    return render(request, 'booktest/child.html')


def html_escape(request):
    return render(request,'booktest/html_escape.html',{'content':'<h1>Hello</h1>'})
