from django.db import models

# Create your models here.


class BookInfo(models.Model):
    """图书模型类"""
    # max_length 指定字符串的长度
    btitle = models.CharField(max_length=20)
    # 出版日期 DataField 日期类型
    bpub_date = models.DateField()


class HeroInfo(models.Model):
    """英雄人物模型类"""
    hnmae = models.CharField(max_length=20)   #英雄名称
    # Fase 默认值 代表男性
    hgender = models.BooleanField(default=False)
    # 备注 
    hcomment = models.CharField(max_length=128)
    # 关系属性 建立图书类和英雄人物类之间的一对多关系
    hbook = models.ForeignKey('BookInfo')
