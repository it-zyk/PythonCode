# 自定义过滤器

# 过滤器就是Python 的函数

from django.template import Library

# 创建一个Library 类的对象
register = Library()


@register.filter
def mod(num):
    '''判断是否为偶数'''
    return num % 2 == 0


@register.filter
def mod_val(num, val):
    '''判断是否整除'''
    return num % val == 0
