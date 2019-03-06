from django.db import models

# Create your models here.

# 1 类


class BookInfoManager(models.Manager):
    '''图书模型管理类'''
    # 1. 改变查询结果集

    def all(self):
        '''改变查询结果集'''
        # 1 调用父类的all 获取所有数据
        books = super().all()
        # 2. 对数据进行过滤
        books = books.filter(is_delete=False)
        return books

    def create_book(self, btitle, bpub_date):
        '''# 模型类： 操作模型类对应的数据表（增删改查）'''
        # 获取self 中的模型类
        models_class = self.models
        book = models_class
        # 创建一个图书对象
        # book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 2. 保存进数据库
        book.save()
        # 3 返回book
        return book


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

    # book = models.Manager()
    objects = BookInfoManager()

    # @classmethod
    # def create_book(cls, btitle, bpub_date):
    #     # 创建图书类对象
    #     obj = cls()
    #     obj.btitle = btitle
    #     obj.bpub_date = bpub_date
    #     # 2.保存进数据库
    #     obj.save()
    #     return obj

    def __str__(self):
        return self.btitle

    class Meta:
        db_table = booktest_bookinfo

# 多类


class HeroInfo(models.Model):
    """英雄人物模型类"""
    hname = models.CharField(max_length=20)  # 英雄名称
    # Fase 默认值 代表男性
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性 建立图书类和英雄人物类之间的   一对多关系
    hbook = models.ForeignKey('BookInfo')

    # 软删除
    is_delete = models.BooleanField(default=False)

    # book = models.Manager() # 自定义

    def __str__(self):
        """返回英雄的名字"""
        return self.hname


# 新闻类型

class NewsType(models.Model):
    # 类型名
    type_name = models.CharField(max_length=20)

    # 关系属性 代表类型下的信息
    type_news = models.ManyToManyField('NewsInfo')


class NewsInfo(models.Model):
    # 新闻标题
    title = models.CharField(max_length=128)
    # 发布类型
    pub_date = models.DateTimeField(auto_now_add=True)

    # 信息内容
    content = models.TextField()

    # 关联关系
    new_type = models.ManyToManyField('NewsType')


class EmployeeBasicInfo(models.Model):
    # 姓名
    name = models.CharField(max_length=20)

    # 性别
    gender = models.BooleanField(default=False)

    # 年龄
    age = models.IntegerField()

    employee_data = models.OneToOneField('EmployeeDetailInfo')


class EmployeeDetailInfo(models.Model):
    # 联系地址
    addr = models.CharField(max_length=256)
    # 关系属性，代表员工基本信息
    employee_basic = models.OneToOneField('EmployeeBasicInfo')


class AreaInfo(models.Model):
    '''地区模型类'''
    atitle = models.CharField(max_length=30)
    # 关系属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank='True')
