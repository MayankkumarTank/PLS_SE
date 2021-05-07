"""PLdscdss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('facultyfeedback/<slug:course_id>',views.facultyfeedback,name='facultyfeedback'),
    path('facultyfeedback/<slug:faculty_id>/<slug:course_id>/submitfacultyfeedback',views.submitfacultyfeedback,name='submitfacultyfeedback'),
    path('coursefeedback/<slug:course_id>',views.coursefeedback,name='coursefeedback'),
    path('coursefeedback/<slug:course_id>/submitcoursefeedback',views.submitcoursefeedback,name='submitcoursefeedback'),
    path('course/<slug:course_id>/task/<slug:task_id>/addsubmission',views.addsubmission,name='addsubmission'),
    path('course/<slug:course_id>/task/<slug:task_id>/addsubmission/submitsubmission',views.submitsubmission,name='submitsubmission'),
    path('dashboard/<slug:course_id>/tasks/viewtask/<slug:task_id>/Grade/<slug:submission_id>/addcomment',views.addcomment,name='addcomment'),
]
