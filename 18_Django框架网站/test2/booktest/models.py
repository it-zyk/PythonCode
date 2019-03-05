from django.db import models

# Create your models here.

# 1 类
class BookInfo(models.Model):
    """图书模型类"""
    # max_length 指定字符串的长度
    btitle = models.CharField(max_length=20)
    # 出版日期 DataField 日期类型
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 软删除
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle

# 多类
class HeroInfo(models.Model):
    """英雄人物模型类"""
    hname = models.CharField(max_length=20)   #英雄名称
    # Fase 默认值 代表男性
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性 建立图书类和英雄人物类之间的   一对多关系
    hbook = models.ForeignKey('BookInfo')


    def __str__(self):
        """返回英雄的名字"""
        return self.hname
