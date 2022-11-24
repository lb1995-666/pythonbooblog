"""Django_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app01 import views
from django.urls import path
app_name = 'app01'
urlpatterns = [
    path(r'blog_detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path(r'', views.blog_index, name='blog_index'),
    path(r'python_base/', views.python_base, name='python_base'),
    path(r'blog_login/', views.blog_login, name='blog_login'),
    path(r'blog_logout/', views.blog_logout, name='blog_logout'),
    path(r'django_frame/', views.django_frame, name='django_frame'),
    path(r'linux_order/', views.linux_order, name='linux_order'),
    path(r'leave_messages/', views.leave_messages, name='leave_messages'),
    path(r'about/', views.about, name='about'),
    path(r'blog_user_info/', views.blog_user_info, name='blog_user_info'),
    path(r'blog_register/', views.blog_register, name='blog_register'),
    path(r'password_change/', views.password_change, name='password_change'),
    path(r'publish_article/', views.publish_article, name='publish_article'),
    path(r'like/<int:blog_id>/', views.like, name='like'),
    path(r'like_comment/<int:comment_id>/<int:blog_id>/', views.like_comment, name='like_comment'),

]
