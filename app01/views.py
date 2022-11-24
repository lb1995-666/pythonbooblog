from django.shortcuts import render, redirect
from django.http import JsonResponse
from app01 import models
import datetime
import hashlib
import os
from Django_pro import settings
# Create your views here.


def search(request):
    formsearch = ''
    if request.method == "POST":
        formsearch = request.POST.get('formsearch')
        # 模糊查询
        if formsearch is None:
            formsearch = ''
    return formsearch


def hash_code(s, salt='app01'):
    # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def blog_index(request):
    log_status = request.session.get('is_login', None)
    if log_status is True:
        username = request.session['user_name']
        user_id = request.session['user_id']
        imgs = models.Users.objects.get(id=user_id)
        img = imgs.head_portrait
        if img == '':
            img = 'photo/default_head_portrait.jpg'

    blogs = models.Blog.objects.filter(title__contains=search(request)).order_by('-id',)
    return render(request, 'app01/blog_index.html', locals())


def python_base(request):
    log_status = request.session.get('is_login', None)
    if log_status is True:
        username = request.session['user_name']
        user_id = request.session['user_id']
        imgs = models.Users.objects.get(id=user_id)
        img = imgs.head_portrait
        if img == '':
            img = 'photo/default_head_portrait.jpg'

    blogs = models.Blog.objects.filter(type="0").filter(title__contains=search(request)).order_by('-id',)
    return render(request, 'app01/python_base.html', locals())


def blog_detail(request, blog_id):
    log_status = request.session.get('is_login', None)
    if log_status is True:
        username = request.session['user_name']
        user_id = request.session['user_id']
        imgs = models.Users.objects.get(id=user_id)
        img = imgs.head_portrait
        nickname = imgs.nickname
        if img == '':
            img = 'photo/default_head_portrait.jpg'
        if request.method == "POST":
            comment = request.POST.get('comment')
            commer = nickname
            if commer == '':
                commer = username
            s = models.BlogComment(comment_context=comment, blog_id_id=blog_id, user_id_id=user_id,
                                   comment_head_portrait=img, commer=commer,
                                   create_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            s.save()
            count = len(models.BlogComment.objects.filter(blog_id=blog_id))
            models.Blog.objects.filter(id=blog_id).update(count=count)
    blogs = models.Blog.objects.filter(id=blog_id)
    creator = blogs[0].creator
    body = blogs[0].body
    title = blogs[0].title
    create_time = blogs[0].create_time
    views = blogs[0].views
    like_num = blogs[0].like_num
    models.Blog.objects.filter(id=blog_id).update(views=views + 1)
    comments = models.BlogComment.objects.filter(blog_id=blog_id).order_by('-like_comment', '-id')
    return render(request, 'app01/blog_detail.html', locals())


def blog_user_info(request):
    log_status = request.session.get('is_login', None)
    if log_status is True:
        username = request.session['user_name']
        user_id = request.session['user_id']
        user = models.Users.objects.filter(id=user_id)[0]
        img = user.head_portrait
        if img == '':
            img = 'photo/default_head_portrait.jpg'
        email = user.email
        phone = user.phone
        nickname = user.nickname
        if request.method == "POST":
            fp = request.FILES.get("file")
            try:
                path1 = os.path.join(settings.MEDIA_ROOT, 'photo/' + fp.name)
                with open(path1, 'wb') as f:
                    f.write(fp.read())
                url = 'photo/{}'.format(fp.name)
            except:
                url = img
            nickname = request.POST.get('nickname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            models.Users.objects.filter(id=user_id).update(nickname=nickname, email=email, phone=phone,
                                                           head_portrait=url)
            msg = '修改成功'
            img = url
            return render(request, "app01/blog_user_info.html", locals())
    return render(request, "app01/blog_user_info.html", locals())


def blog_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = models.Users.objects.get(username=username)
        except:
            msg = "用户不存在"
            return render(request, 'app01/blog_login.html', locals())
        if user.password == hash_code(password):
            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.username
            request.session['nickname'] = user.nickname
            return redirect('/')
        else:
            msg = "密码错误"
            return render(request, 'app01/blog_login.html', locals())

    return render(request, 'app01/blog_login.html', locals())


def blog_logout(request):
    if not request.session.get('is_login', None):
        return JsonResponse({'msg': 'logout fail, not login'})
    request.session.flush()
    # msg = '注销成功'
    return redirect('/')
    pass


def blog_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        models.Users.objects.create(username=username, password=hash_code(password), email=email, phone=phone,
                                    create_date=datetime.datetime.now().strftime('%Y-%m-%d'))
        msg = "注册成功"
        return render(request, 'app01/blog_register.html', locals())
    return render(request, 'app01/blog_register.html', locals())


def django_frame(request):
    log_status = request.session.get('is_login', None)
    if log_status is True:
        username = request.session['user_name']
        user_id = request.session['user_id']
        imgs = models.Users.objects.get(id=user_id)
        img = imgs.head_portrait
        if img == '':
            img = 'photo/default_head_portrait.jpg'
    blogs = models.Blog.objects.filter(type="1").filter(title__contains=search(request)).order_by('-id',)
    return render(request, 'app01/django_frame.html', locals())


def linux_order(request):
    log_status = request.session.get('is_login', None)
    if log_status is True:
        username = request.session['user_name']
        user_id = request.session['user_id']
        imgs = models.Users.objects.get(id=user_id)
        img = imgs.head_portrait
        if img == '':
            img = 'photo/default_head_portrait.jpg'
    blogs = models.Blog.objects.filter(type="4").filter(title__contains=search(request)).order_by('-id',)
    return render(request, 'app01/linux_order.html', locals())


def leave_messages(request):
    log_status = request.session.get('is_login', None)
    if log_status is True:
        username = request.session['user_name']
        user_id = request.session['user_id']
        imgs = models.Users.objects.get(id=user_id)
        img = imgs.head_portrait
        if img == '':
            img = 'photo/default_head_portrait.jpg'
        if request.method == "POST":
            u_name = request.POST.get("u_name")
            u_email = request.POST.get("u_email")
            u_context = request.POST.get("u_context")
            new_obj = models.LeaveMessage(u_name=u_name, u_email=u_email, u_context=u_context,
                                          create_time=datetime.datetime.now(), leave_user=username)
            new_obj.save()
            msg = "提交成功"
    else:
        msg = "请先登录"
    return render(request, 'app01/leave_messages.html', locals())


def about(request):
    log_status = request.session.get('is_login', None)
    if log_status is True:
        username = request.session['user_name']
        user_id = request.session['user_id']
        imgs = models.Users.objects.get(id=user_id)
        img = imgs.head_portrait
        if img == '':
            img = 'photo/default_head_portrait.jpg'
    return render(request, 'app01/about.html', locals())


def password_change(request):
    log_status = request.session.get('is_login', None)
    if log_status is True:
        username = request.session['user_name']
        user_id = request.session['user_id']
        imgs = models.Users.objects.get(id=user_id)
        img = imgs.head_portrait
        if img == '':
            img = 'photo/default_head_portrait.jpg'
        if request.method == "POST":
            old_password = request.POST.get("old_password")
            new_password1 = request.POST.get("new_password1")
            new_password2 = request.POST.get("new_password2")
            user = models.Users.objects.get(id=user_id)
            if user.password == hash_code(old_password):
                if new_password1 == new_password2:
                    models.Users.objects.filter(id=user_id).update(password=hash_code(new_password1))
                    msg = '修改密码成功'
                    return render(request, 'app01/password_change.html', locals())
                else:
                    err_msg = '两次输入密码不一致'
                    return render(request, 'app01/password_change.html', locals())
            else:
                err_msg = '旧密码错误'
                return render(request, 'app01/password_change.html', locals())
    else:
        err_msg = '请先登陆'
    return render(request, 'app01/password_change.html', locals())


def publish_article(request):
    log_status = request.session.get('is_login', None)
    types = models.Blog.types
    if log_status is True:
        username = request.session['user_name']
        user_id = request.session['user_id']
        imgs = models.Users.objects.get(id=user_id)
        img = imgs.head_portrait
        nickname = imgs.nickname
        if nickname == '':
            nickname = username
        if img == '':
            img = 'photo/default_head_portrait.jpg'
        if request.method == "POST":
            title = request.POST.get("title")
            type = request.POST.get("type")
            creator = nickname
            body = request.POST.get("body")
            new_obj = models.Blog(title=title, type=type, creator=creator,
                                  create_time=datetime.datetime.now(), body=body)
            new_obj.save()
            msg = "提交成功"
            return redirect('/')
    else:
        msg = "请先登录"
    return render(request, 'app01/publish_article.html', locals())


def like(request, blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    like_num = blog.like_num
    models.Blog.objects.filter(id=blog_id).update(like_num=like_num + 1)
    return redirect('/blog_detail/{}/'.format(blog_id))


def like_comment(request, comment_id, blog_id):
    blogcomment = models.BlogComment.objects.get(id=comment_id)
    like_comment = blogcomment.like_comment
    models.BlogComment.objects.filter(id=comment_id).update(like_comment=like_comment + 1)
    return redirect('/blog_detail/{}/'.format(blog_id))



