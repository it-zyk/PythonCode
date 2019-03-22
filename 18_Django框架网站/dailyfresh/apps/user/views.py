from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import re
from user.models import User
from django.views.generic import View
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from celery_tasks.tasks import send_register_active_email

# Create your views here.


class RegisterView(View):
    '''注册类视图'''

    def get(self, request):
        '''显示注册页面'''
        return render(request, 'user/register.html')

    def post(self, request):
        '''进行注册处理'''
        # 1.接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        if allow != 'on':
            return render(request, 'user/register.html', {'errmsg': '请同意协议'})
        # 2. 进行数据校验
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'user/register.html', {'errmsg': '注册信息不完整'})
        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'user/register.html', {'errmsg': '邮箱格式不合法'})

        # 3. 进行业务处理： 进行用户注册
        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            return render(request, 'user/register.html', {'errmsg': '用户名已存在'})

        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        # 发送激活邮件，包含激活链接: http://127.0.0.1:8000/user/active/3
        # 激活链接中需要包含用户的身份信息, 并且要把身份信息进行加密

        # 加密用户的身份信息，生成激活token
        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': user.id}
        token = serializer.dumps(info)  # bytes
        token = token.decode()

        # 发邮件
        send_register_active_email.delay(email, username, token)

        # 4，返回应答 跳转首页
        return redirect(reverse('goods:index'))


class LoginView(View):
    '''登录页面'''

    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        pass


class ActiveView(View):
    '''用户激活'''

    def get(self, request, token):
        '''进行用户激活'''
        # 进行解密，获取要激活的用户信息
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            # 获取待激活用户的id
            user_id = info['confirm']

            # 根据id获取用户信息
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            # 跳转到登录页面
            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            # 激活链接已过期
            return HttpResponse('激活链接已过期')


# GET POST PUT DELETE OPTION
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        # 1.接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        if allow != 'on':
            return render(request, 'user/register.html', {'errmsg': '请同意协议'})
        # 2. 进行数据校验
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'user/register.html', {'errmsg': '注册信息不完整'})
        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'user/register.html', {'errmsg': '邮箱格式不合法'})

        # 3. 进行业务处理： 进行用户注册
        # 校验用户名是否重复
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            return render(request, 'user/register.html', {'errmsg': '用户名已存在'})

        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()
        # 4，返回应答 跳转首页
        # 加密用户的身份信息，生成激活token
        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': user.id}
        token = serializer.dumps(info)  # bytes
        token = token.decode()

        # 发邮件
        send_register_active_email.delay(email, username, token)

        return redirect(reverse('goods:index'))


def register_handle(request):
    '''进行注册处理'''

    # 1.接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')
    if allow != 'on':
        return render(request, 'user/register.html', {'errmsg': '请同意协议'})
    # 2. 进行数据校验
    if not all([username, password, email]):
        # 数据不完整
        return render(request, 'user/register.html', {'errmsg': '注册信息不完整'})
    # 校验邮箱
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'user/register.html', {'errmsg': '邮箱格式不合法'})

    # 3. 进行业务处理： 进行用户注册
    # 校验用户名是否重复
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        # 用户名不存在
        user = None

    if user:
        return render(request, 'user/register.html', {'errmsg': '用户名已存在'})

    user = User.objects.create_user(username, email, password)
    user.is_active = 0
    user.save()
    # 4，返回应答 跳转首页
    return redirect(reverse('goods:index'))
