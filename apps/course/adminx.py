# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx
   Description :
   Author :       huang
   date：          2018/7/2
-------------------------------------------------
   Change Activity:
                   2018/7/2:
-------------------------------------------------
"""
__author__ = 'huang'

import xadmin

from .models import Course, Chapter, CourseSource, Video


class CourseAdmin:

    list_display = ["name", "description", "detail", "degree", "learning_times", "students", "collect_nums",
                    "click_nums", "image", "create_time"]
    search_fields = ["name", "description", "detail", "degree", "learning_times", "students", "collect_nums",
                     "click_nums"]
    list_filter = ["name", "description", "detail", "degree", "learning_times", "students", "collect_nums",
                   "click_nums", "image", "create_time"]


class ChapterAdmin:

    list_display = ["name", "create_time", "course"]
    search_fields = ["name", "create_time", "course__name"]
    list_filter = ["name", "create_time", "course__name"]


class VideoAdmin:

    list_display = ["name", "create_time", "chapter"]
    search_fields = ["name", "create_time", "chapter__name"]
    list_filter = ["name", "create_time", "chapter__name"]


class CourseSourceAdmin:

    list_display = ["name", "create_time", "course"]
    search_fields = ["name", "create_time", "course__name"]
    list_filter = ["name", "create_time", "course__name"]

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseSource, CourseSourceAdmin)