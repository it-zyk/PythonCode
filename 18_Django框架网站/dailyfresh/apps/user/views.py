from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import re
from user.models import User
# Create your views here.


def register(request):
    return render(request, 'user/register.html')


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
    redirect(reverse('goods.index'))
