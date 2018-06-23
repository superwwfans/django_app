
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户信息表
    """
    nick_name = models.CharField(max_length=50, default="", verbose_name="昵称")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    gender = models.CharField(choices=(("male", "男"), ("male", "女")), default="female", max_length=5)
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="images/%Y/%m", default="images/default.png", max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    """
    轮播图
    """
    title = models.CharField(max_length=50, verbose_name='标题')
    image_url = models.URLField(max_length=200, verbose_name="图片URL")
    image_upload_path = models.FileField(upload_to='banner/%Y-%m', max_length=100, verbose_name="图片上传路径")
    index = models.CharField(max_length=10, default="10", verbose_name="图片顺序")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    """
    邮箱验证码
    """
    verify_code = models.CharField(max_length=20, verbose_name="邮箱验证码")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")
    email_address = models.EmailField(max_length=250, verbose_name="邮箱地址")
    send_email_type = (
        ("Register", "注册"),
        ("Forget", "忘记密码")
    )
    send_type = models.CharField(max_length=10, choices=send_email_type, verbose_name="发送类型")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name
