from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse

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
