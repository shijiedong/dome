# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

"""


"""

class T1_Task(models.Model):
    strName   = models.CharField(max_length=20)             # 任务名称
    nTaskID   = models.IntegerField(default = 0)            # 当前任务ID
    nStatu    = models.IntegerField(default = 2)            # 当前任务状态，
    create_at = models.DateTimeField(auto_now_add=True)     # 创建时间
    update_at = models.DateTimeField(auto_now=True)         # 更新时间

    def __unicode__(self):
        return self.strName

class T2_MoneyApplyFor(models.Model):                       # 任务ID 1001
    nTaskID  = models.IntegerField()                        # 当前任务ID
    nStatu   = models.IntegerField( default = 1 )           # 当前任务状态  

    nMoney   = models.IntegerField( default = 0 )           # 金额
    strNode  = models.CharField( max_length = 200 )         # 备注

    create_at = models.DateTimeField(auto_now_add=True)     # 创建时间
    update_at = models.DateTimeField(auto_now=True)         # 更新时间

    def __unicode__(self):
        return self.strNode


class T2_TestTask(models.Model):                            # 任务ID 1002
    nTaskID = models.IntegerField()                         # 当前任务ID
    nStatus = models.IntegerField( default = 1 )            # 当前任务状态

    nMoney  = models.IntegerField( default = 0 )            # 金额
    strNode = models.CharField( max_length = 200 )          # 备注

    create_at = models.DateTimeField(auto_now_add=True)     # 创建时间
    update_at = models.DateTimeField(auto_now=True)         # 更新时间

    def __unicode__(self):
        return self.strNode
