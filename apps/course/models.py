
from datetime import datetime

from django.db import models


class Course(models.Model):
    """
    课程
    """
    name = models.CharField(max_length=100, verbose_name="课程名称")
    description = models.CharField(max_length=200, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")

    course_level = (
        ("Basic", "初级"),
        ("Intermediate", "中级"),
        ("Advanced", "高级"),
    )
    degree = models.CharField(max_length=20, choices=course_level, verbose_name="课程等级")
    learning_times = models.IntegerField(verbose_name="学习时长")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    collect_nums = models.IntegerField(default=0, verbose_name="收藏数")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    image = models.ImageField(upload_to="courses/%Y-%m", verbose_name="课程封面")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name


class Chapter(models.Model):
    """
    课程下的章节
    """
    name = models.CharField(max_length=100, verbose_name="章节名称")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="章节课程")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name


class Video(models.Model):
    """
    章节下的视频
    """
    name = models.CharField(max_length=100, verbose_name="视频名称")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "章节视频"
        verbose_name_plural = verbose_name


class CourseSource(models.Model):
    """
    课程资源
    """
    name = models.CharField(max_length=100, verbose_name="资源名称")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name
