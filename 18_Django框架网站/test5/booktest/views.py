from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.conf import settings

EXCLUDE_IPS = ['10.2.34.36']


def blocked_ips(view_func):
    def wrapp(request, *view_args, **view_kwargs):
        # 获取浏览器端的ip地址
        addr = request.META['REMOTE_ADDR']
        if addr in EXCLUDE_IPS:
            return HttpResponse('Forbidden')
        else:
            return view_func(request, *view_args, **view_kwargs)
    return wrapp


# @blocked_ips
# 使用中间件函数替代装饰器
def index(request):
    '''首页'''
    print('----------index---------------')
    # num = 'a' + 1
    return render(request, 'booktest/index.html')


def static_test(request):
    '''静态文件'''

    return render(request, 'booktest/static_test.html')
