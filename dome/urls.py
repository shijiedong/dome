"""dome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import shane.views as dome_task

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^task/', dome_task.create_task),
    url(r'^rout/', dome_task.task_router),
    url(r'^add1001/', dome_task.task_1001),
    url(r'^add1002/', dome_task.task_1002),
]
