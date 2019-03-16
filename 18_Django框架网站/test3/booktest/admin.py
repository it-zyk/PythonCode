from django.contrib import admin
from booktest.models import BookInfo, HeroInfo
# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment']


class HeroInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ['id', 'hname', 'hcomment']


# Register your models here.
# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
