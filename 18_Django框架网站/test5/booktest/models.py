from django.db import models

# Create your models here.


class AreaInfo(models.Model):
    '''地区模型类'''

    # 地区名称
    atitle = models.CharField(verbose_name='标题', max_length=20)

    # 自定义关联
    aParent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle

    def parent(self):
        if self.aParent.atitle is None:
            return ''
        else:
            return self.aParent.atitle

    parent.short_description = '父级地区'

    title.admin_order_field = 'atitle'
    title.short_description = '地区名称'


class PicTest(models.Model):
    '''上传图片'''
    goods_pic = models.ImageField(upload_to='booktest')
