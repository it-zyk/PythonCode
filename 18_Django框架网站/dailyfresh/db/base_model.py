from django.db import models


class BaseModel(models.Model):
    '''模型抽象基类'''
    create_time = models.DateTimeField(auto_now_add=True, verbase_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True, verbase_name='更新时间')
    is_delete = models.BooleanField(default=False, verbase_name="删除标识")

    class Meta:
        abstract = True  # 说明是一个抽象类
