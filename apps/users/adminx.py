# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx
   Description :
   Author :       huang
   date：          2018/7/1
-------------------------------------------------
   Change Activity:
                   2018/7/1:
-------------------------------------------------
"""
__author__ = 'huang'

import xadmin

from .models import  EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin:

    list_display = ["verify_code", "email_address", "send_type", "send_time"]
    search_fields = ["verify_code", "email_address", "send_type"]
    list_filter = ["verify_code", "email_address", "send_type", "send_time"]


class BannerAdmin:

    list_display = ["title", "image_url", "image_upload_path", "index", "create_time"]
    search_fields = ["title", "image_url", "image_upload_path", "index"]
    list_filter = ["title", "image_url", "image_upload_path", "index", "create_time"]

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)