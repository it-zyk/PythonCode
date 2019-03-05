from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

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

    return render(request, 'booktest/index.html', {'content' : 'Hello world!', 'list': list(range(1, 10))})


    
