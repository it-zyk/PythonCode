from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from booktest.models import BookInfo
# Create your views here.

# /index


def login_required(view_func):
    '''登录判断装饰器'''
    def wrapper(request, *view_args, **view_kwargs):
        # 判断用户是否登录
        if request.session.has_key('islogin'):
            # 用户已登录,调用对应的视图
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录，跳转登录页
            return redirect('/login')
    return wrapper


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


def login(request):
    '''登陆'''
    # 获取登陆过的用户名
    if request.session.has_key('islogin'):
        return redirect('/change_pwd')
    else:
        if 'username' in request.COOKIES:
            # 获取记住的用户名
            username = request.COOKIES['username']
        else:
            username = ''

    return render(request, 'booktest/login.html', {"username": username})

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
    # 获取用户输入的验证码
    vcode = request.POST.get('vcode')

    # 获取session中保存的验证码
    vcode2 = request.session.get('verifycode')

    # 进行验证码的校验
    if vcode.lower() != vcode2.lower():
        return redirect('/login')

    # 2. 进行登录校验
    # 数据库验证
    if username == 'smart' and password == '123':
        # 跳转到首页
        # 判断是否要记住用户名
        response = redirect("/index")
        response = redirect("/change_pwd")

        if remember == 'on':
            response.set_cookie('username', username, max_age=7 * 24 * 3600)
        request.session['islogin'] = True
        # 记住登录的用户名
        request.session['username'] = username
        # 返回应答
        return response

    else:
        redirect("/login")

    # 3. 返回应答


@login_required
def change_pwd(request):
    '''显示修改密码'''
    return render(request, 'booktest/change_pwd.html')


@login_required
def change_pwd_action(request):
    '''获取新密码'''
    username = request.session.get("username")
    pwd = request.POST.get('pwd')
    return HttpResponse('%s 修改密码为：%s' % (username, pwd))


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
    return render(request, 'booktest/html_escape.html', {'content': '<h1>Hello</h1>'})


from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

# /verify_code


def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高 RGB
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # font = ImageFont.truetype('FreeMono.ttf', 23)
    font = ImageFont.truetype('arial.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def url_reverse(request):
    '''url 反向解析页面 '''
    return render(request, 'booktest/url_reverse.html')


def show_args(request, a, b):
    return HttpResponse(a + ':' + b)


def show_kwargs(request, c, d):
    return HttpResponse(c + ':' + d)


from django.core.urlresolvers import reverse


def test_redirect(request):
    '''重定向到首页'''
    url = reverse('booktest:index')

    # 重定向 show_args/1/2
    url = reverse('booktest:show_args', args=(1, 2))

    # 重定向 show_args/1/2
    url = reverse('booktest:show_kwargs', kwargs={'c': 3, 'd': 4})
    return redirect(url)
