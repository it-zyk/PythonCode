from django.db import models

# Create your models here.


class BookInfo(models.Model):
    """图书模型类"""
    # max_length 指定字符串的长度
    btitle = models.CharField(max_length=20)
    # 出版日期 DataField 日期类型
    bpub_date = models.DataField()
