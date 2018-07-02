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

from .models import UserAsk, UserCollect, UserCourse, UserMessage, CourseComment


class UserAskAdmin:

    list_display = ["name", "course_name", "mobile", "add_time"]
    search_fields = ["name", "course_name", "mobile"]
    list_filter = ["name", "course_name", "mobile", "add_time"]


class UserCollectAdmin:

    list_display = ["user", "collect_id", "collect_type", "create_time"]
    search_fields = ["user", "collect_id", "collect_type", "create_time"]
    list_filter = ["user", "collect_id", "collect_type", "create_time"]


class UserCourseAdmin:

    list_display = ["user", "course", "create_time"]
    search_fields = ["user", "course"]
    list_filter = ["user", "course", "create_time"]


class UserMessageAdmin:

    list_display = ["user", "message", "is_read", "send_time"]
    search_fields = ["user", "message", "is_read", "send_time"]
    list_filter =["user", "message", "is_read", "send_time"]


class CourseCommentAdmin:

    list_display = ["course", "user", "comments", "create_time"]
    search_fields = ["course", "user", "comments", "create_time"]
    list_filter = ["course", "user", "comments", "create_time"]


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCollect, UserCollectAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)