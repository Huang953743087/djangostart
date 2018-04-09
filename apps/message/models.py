#-*-coding:utf-8-*-
from django.db import models

# Create your models here.

class UserMessage(models.Model):
    #orm max_length最大长度,verbos_name应该是字段名
    name = models.CharField(max_length=10, null=True, blank=True, verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=30, verbose_name=u'地址')
    message = models.CharField(max_length=200, verbose_name=u'信息')
    object_id = models.CharField(primary_key=True, max_length=30, default='', verbose_name='主键')

    class Meta:
        verbose_name = u'用户留言信息'
        ordering = ('-object_id',)
        verbose_name_plural = u'用户留言信息'
