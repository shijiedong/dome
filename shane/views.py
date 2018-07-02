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
	task_name 	= request.POST.get('task_name', 'null')
	task_id 	= request.POST.get('task_id', 0)
	print task_name
	print task_id
	task = models.T1_Task.objects.create(strName=task_name, nTaskID=task_id )
	print "taskid:%d" % task.id 

	if( 1001 == task_id ):
		pass
		#return render( request, "financial.html", { 'taskid' : task.id })
	elif( 1002 == task_id):
		pass
		#return render( request, "financial.html", { 'taskid' : task.id })
	elif( 1003 == task_id ):
		pass
		#return render( request, "financial.html", { 'taskid' : task.id })
	return render( request, "financial.html", { 'taskid' : task.id })

def task_1001(request,task_id):
	strname = request.POST.get('name', 'null')
	strtype = request.POST.get('type', 'nill')
	print strname
	print strtype
	models.T2_MoneyApplyFor.objects.create( strName=strname, strType=strtype )

	return render( request, "financial.html")

def task_1002(request,task_id):
	strname = request.POST.get('name', 'null')
	strtype = request.POST.get('type', 'nill')
	print strname
	print strtype

	models.T2_TestTask.objects.create(strName=strname, strType=strtype )
	return render( request, "financial.html")


