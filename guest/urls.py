from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('schools/<str:s_name>/', views.school, name='school_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.Logout, name='logout'),
    path('course/<str:course>/', views.course, name='course_page'),
    path('processing_login/', views.after_login, name='after_login'),
]