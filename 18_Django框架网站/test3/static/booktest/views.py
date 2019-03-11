from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    # request.Path
    return render(request, 'booktest/index.html')

# request 包含浏览器的信息，num 参数信息


def show_arg(request, num):
    return HttpResponse(num)


def login(request):
    return render(request, 'booktest/login.html')

# 返回 QueryDict


def login_check(request):
    '''登录较正'''
    # 1 .获取提交的用户名和密码
    # request.POST 保存post 提交的参数
    # request.GET 保存get 提交的参数
    # print(type(request.POST))
    # request.method  POST/GET
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2. 进行登录校验
    # 数据库验证
    if username == 'smart' and password == '123':
        # 跳转到首页
        redirect("/index")
    else:
        redirect("/login")

    # 3. 返回应答


def ajax_test(request):
    '''显示ajax页面 '''
    return render(request, "booktest/test_ajax.html")


def ajax_handle(request):
    '''ajax处理请求'''
    # 返回json数据
    retun JsonResponse({'res': 1})
