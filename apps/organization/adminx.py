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

from .models import Organization, City, Teacher


class CityAdmin:
    list_display = ["name",  "create_time"]

    search_fields = ["name"]

    list_filter = ["name",  "create_time"]



class OrganizationAdmin:

    list_display = ["name", "describe", "image", "address", "collect_nums",
                    "click_nums", "create_time", "city"]

    search_fields = ["name", "describe", "image", "address", "collect_nums",
                     "click_nums", "city__name"]

    list_filter = ["name", "describe", "image", "address", "collect_nums",
                   "click_nums", "create_time", "city__name"]


class TeacherAdmin:

    list_display = ["name", "work_year", "work_company", "position", "feature", "organization", "collect_nums",
                    "click_nums", "create_time"]

    search_fields = ["name", "work_year", "work_company", "position", "feature", "organization__name", "collect_nums",
                     "click_nums"]

    list_filter = ["name", "work_year", "work_company", "position", "feature", "organization__name", "collect_nums",
                   "click_nums", "create_time"]


xadmin.site.register(Organization, OrganizationAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(City, CityAdmin)