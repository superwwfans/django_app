from datetime import datetime

from django.db import models


class Organization(models.Model):
    """
    组织机构
    """
    name = models.CharField(max_length=100, verbose_name="机构名称")
    describe = models.TextField(verbose_name="机构简介")
    image = models.ImageField(upload_to="org/%Y-%d", verbose_name="机构封面")
    address = models.CharField(max_length=200, verbose_name="机构地址")
    click_nums = models.IntegerField(verbose_name="点击数")
    collect_nums = models.IntegerField(verbose_name="收藏数")
    create_time = models.DateTimeField(default=datetime.now)

    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    class Meta:
        verbose_name = "组织机构"
        verbose_name_plural = verbose_name


class City(models.Model):
    """
    机构所在城市信息
    """
    name = models.CharField(max_length=50, verbose_name="城市名称")
    create_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "城市信息"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    """
    机构教师信息
    """
    name = models.CharField(max_length=50, verbose_name="教师姓名")
    work_year = models.IntegerField(max_length=10, verbose_name="工龄")
    work_company = models.CharField(max_length=20, verbose_name="工作单位")
    position = models.CharField(max_length=20, verbose_name="职位")
    feature = models.CharField(max_length=100, verbose_name="教学特点")
    click_nums = models.IntegerField(verbose_name="点击数")
    collect_nums = models.IntegerField(verbose_name="收藏数")
    create_time = models.DateTimeField(default=datetime.now)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "教师信息"
        verbose_name_plural = verbose_name