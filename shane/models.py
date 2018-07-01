# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TaskMain(models.Model):
	strName = models.CharField(max_length=10)
	strType = models.CharField(max_length=10)

