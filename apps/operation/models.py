
from datetime import datetime

from django.db import models

from course.models import Course
from users.models import UserProfile


class UserAsk(models.Model):
    """
    用户咨询
    """
    name = models.CharField(max_length=50, verbose_name="姓名")
    course_name = models.CharField(max_length=50, verbose_name="课程名")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


class CourseComment(models.Model):
    """
    用户对课程的评论
    """
    course = models.ForeignKey(Course, verbose_name="课程")
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    comments = models.CharField(max_length=200, verbose_name="评论")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")


    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name


class UserCollect(models.Model):
    """
    用户收藏的课程,机构,讲师
    """
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    collect_id = models.IntegerField(default=0, verbose_name="数据id")  # 存储课程,机构, 讲师的id
    collects = (
        (1, "课程"),
        (2, "课程机构"),
        (3, "讲师"),
    )
    collect_type = models.CharField(max_length=10, choices=collects, default=1, verbose_name="收藏类型")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    """
    用户消息
    """
    user = models.IntegerField(default=0, verbose_name="用户")   # 存储用户的id 0为全部用户
    message = models.CharField(max_length=500, verbose_name="消息内容")
    is_read = models.BooleanField(default=False, verbose_name="是否已读")  # False未读, True已读
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    """
    用户学习的课程
    """
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    course = models.ForeignKey(Course, verbose_name="课程")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

