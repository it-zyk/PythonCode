from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from datetime import datatime, timedelta


def index(request):
    # request.Path
    return render(request, 'booktest/index.html')

# request 包含浏览器的信息，num 参数信息


def show_arg(request, num):
    return HttpResponse(num)


def login(request):
    '''登陆'''
    # 获取登陆过的用户名
    if 'username' in request.COOKIES:
        # 获取记住的用户名
        username = request.COOKIES['username']
    else:
        username = ''

    return render(request, 'booktest/login.html', username=username)

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

    remember = request.POST.get('remember')

    # 2. 进行登录校验
    # 数据库验证
    if username == 'smart' and password == '123':
        # 跳转到首页
        # 判断是否要记住用户名
        response = redirect("/index")
        if remember == 'on':
            response.set_cookie('username', username, max_age=7 * 24 * 3600)

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


def set_cookie(request):
    '''设置cookies'''
    response = HttpResponse('设置cookies')
    # response.set_cookie('num', 1)
    # response.set_cookie('num', 1, max_age=14*24 *3600)
    # 设置cookies 由有效时间
    response.set_cookie('num', 1, expires=datetime.now() + timedelta(days=14))
    retun response


def get_cookie(request):
    '''获取cookies'''
    num = request.COOKIES('num')
    retun HttpResponse(num)


# /set_session
def set_session(request):
    '''设置session'''
    request.session['username'] = 'smart'
    request.session['age'] = 18
    # request.session.set_expiry(5)
    return HttpResponse('设置session')


# /get_session
def get_session(request):
    '''获取session'''
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+':'+str(age))


#　/clear_session
def clear_session(request):
    '''清除session信息'''
    # request.session.clear()
    request.session.flush()
    return HttpResponse('清除成功')
