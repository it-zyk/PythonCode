from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
from django.conf import settings

from booktest.models import PicTest, AreaInfo


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


def show_upload(request):
    '''显示上传图片页面'''
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    '''上传图片处理'''
    # 1 获取上传的图片
    pic = request.FILES['pic']

    # 上传文件不大于2.5M,放入内存中
    # 上传文件大于2.5M，放入临时文件
    # pic.name
    # pic.chunks()

    # 2. 创建一个文件
    save_path = '%s/booktest/%s' % (settings.MEDIA_ROOT, pic.name)

    with open(save_path, 'wb') as f:
        for content in pic.chunks():
            f.write(content)
    # 3. 获取上传文件的内容并写到传教的文件中

    # 4. 在数据库中保存上传记录
    PicTest.objects.create(goods_pic='booktest/%s' % pic.name)
    # 5. 退回

    return HttpResponse('ok')


from django.core.paginator import Paginator

# 前端访问的时候需要传递页面
# show_area


def show_area(request, pindex):
    '''查询所有省级地区的信息'''
    # 1.过滤满足条件信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    if pindex == '':
        pindex = 1
    else:
        pindex = int(pindex)
    # 2. 分页， 每页显示10条
    paginator = Paginator(areas, 10)

    # 获取第一页的内容 Page实例对象
    page = paginator.page(pindex)

    return render(request, 'booktest/show_area.html', {"areas": areas, "page": page})


def areas(request):
    return render(request, 'booktest/areas.html')


# /proc
def prov(request):
    '''返回json数据，省份信息'''
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))
    return JsonResponse({"res": areas_list})


def city(request, provid):
    areas = AreaInfo.objects.filter(aParent__id=provid)
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))
    return JsonResponse({"res": areas_list})
