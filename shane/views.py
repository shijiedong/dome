# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def create_task(request):
    #return HttpResponse("<h1>Create Task</h1>")
    return render( request, "create_task.html")

def task_router(request):
	print "task_router"
	strname = request.POST.get('task_name', 'null')
	strtype = request.POST.get('task_id', 'nill')
	print strname
	print strtype
	task = models.T1_Task.objects.create(strName=strname, nTaskID=strtype )
	print "taskid:%d" % task.id 
	if( strtype == 1001 ):
		return render( request, "financial.html", { 'taskid' : task.id })
	else:
		return render( request, "financial.html", { 'taskid' : task.id })


def task_1001(request, task_id):
	strname = request.POST.get('name', 'null')
	strtype = request.POST.get('type', 'nill')
	print strname
	print strtype
	models.T2_MoneyApplyFor.objects.create(strName=strname, strType=strtype )

	return render( request, "financial.html")

def task_1002(request, task_id):
	strname = request.POST.get('name', 'null')
	strtype = request.POST.get('type', 'nill')
	print strname
	print strtype

	models.T2_TestTask.objects.create(strName=strname, strType=strtype )
	return render( request, "financial.html")


