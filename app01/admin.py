from django.contrib import admin
from .models import Users, Blog, BlogComment, LeaveMessage
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'create_date')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'creator', 'create_time')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ['type', 'create_time']
    list_editable = ('type',)


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_id', 'user_id', 'comment_context', 'create_time')
    list_display_links = ('blog_id',)


class LeaveMessageAdmin(admin.ModelAdmin):
    list_display = ("u_name", "u_email", "u_context", "leave_user", "create_time")


# 修改标题
admin.site.site_header = '后台管理系统'
admin.site.site_title = '后台管理'
admin.site.register(Users, UsersAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(LeaveMessage, LeaveMessageAdmin)



