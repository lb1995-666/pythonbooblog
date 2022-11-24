from django.db import models
from tinymce.models import HTMLField
from DjangoUeditor.DjangoUeditor.models import UEditorField
import datetime
# Create your models here.


class Users(models.Model):
    genders = (
        ('male', "男"),
        ('female', "女"),
    )
    username = models.CharField(max_length=255, verbose_name='用户名')
    password = models.CharField(max_length=255, verbose_name='密码')
    nickname = models.CharField(max_length=255, verbose_name='昵称')
    head_portrait = models.ImageField(verbose_name='头像', upload_to='photo', max_length=100, default=None, blank=False)
    email = models.EmailField(max_length=255, verbose_name='邮箱')
    gender = models.CharField(max_length=32, choices=genders, default='男')
    phone = models.CharField(max_length=32, verbose_name='手机号')
    # user_role = models.ForeignKey('role', on_delete=models.SET_NULL, null=True)
    create_date = models.DateField(verbose_name='创建日期', default=None)

    class Meta:
        verbose_name = '网站用户'
        verbose_name_plural = '网站用户'

    def __str__(self):
        return self.username


class Blog(models.Model):
    types = [
        ("0", "python基础"),
        ("1", "Django框架"),
        ("2", "Flask框架"),
        ("3", "mysql"),
        ("4", "linux常用命令"),
    ]
    title = models.CharField(max_length=255, verbose_name="标题")
    type = models.CharField(max_length=255, choices=types, verbose_name="类型")
    label = models.CharField(max_length=255, verbose_name="标签", blank=True)
    views = models.IntegerField(verbose_name="阅读量", default=0, blank=True)
    count = models.IntegerField(verbose_name="评论量", default=0, blank=True)
    like_num = models.IntegerField(verbose_name="点赞量", default=0, blank=True)
    creator = models.CharField(max_length=255, verbose_name="作者")
    create_time = models.DateTimeField(verbose_name="创建时间", default=datetime.datetime.now())
    context = HTMLField(verbose_name="简介", blank=True)
    body = UEditorField(verbose_name='富文本内容', width=800, height=500,
                        toolbars="full", imagePath="media/photo/", filePath="media/attachment/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, verbose_name="博客id")
    user_id = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, verbose_name="用户id")
    commer = models.CharField(max_length=255, verbose_name="评论者", blank=True, null=True)
    like_comment = models.IntegerField(max_length=255, verbose_name="点赞评论量", blank=True, null=True, default=0)
    comment_context = models.CharField(max_length=255, verbose_name="评论内容")
    create_time = models.DateTimeField(verbose_name="创建时间", default=datetime.datetime.now())
    comment_head_portrait = models.CharField(max_length=255, verbose_name="评论者头像地址",
                                             default='photo/default_head_portrait.jpg')


class LeaveMessage(models.Model):
    u_name = models.CharField(max_length=255, verbose_name="用户姓名")
    u_email = models.CharField(max_length=255, verbose_name="用户邮箱")
    u_context = models.CharField(max_length=2000, verbose_name="用户留言内容")
    create_time = models.DateTimeField(verbose_name="创建时间", default=datetime.datetime.now())
    leave_user = models.CharField(max_length=2000, verbose_name="留言用户",default="")

    class Meta:
        verbose_name = "用户留言内容"
        verbose_name_plural = "用户留言内容"

    def __str__(self):
        return self.u_name

