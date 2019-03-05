from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

from booktest.models import BookInfo  # 导入图书类
# Create your views here.


def my_render(request, temp_path, context_dict={}):
    temp = loader.get_template(temp_path)
    # 定义模板上下文，为模板文件传递数据 {} 字典形式
    context = RequestContext(request, context_dict)
    res_html = temp.reder(context)
    return HttpResponse(res_html)

    # http://localhost:8000/index


def index(request):
    # 进行处理， 和M和T进行交互
    # return HttpResponse('老铁没毛病')
    # 1.加载模板文件
    # 3.模板渲染 产生标准的html内容

    # return my_render(request, 'booktest/index.html')

    return render(request, 'booktest/index.html', {'content': 'Hello world!', 'list': list(range(1, 10))})


def show_books(request):
    '''显示图书的信息'''
    # 1. 通过M查图片表的数据
    books = BookInfo.objects.all()

    return render(request, 'booktest/show_books.html', {'books': books})


def detail(request, bid):
    '''查询图书关联英雄信息'''
    # 1. 根据bid 查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2 查询和book关联的英雄信息
    heros = book.heroinfo_set.all()
    # 3. 使用模板
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})
