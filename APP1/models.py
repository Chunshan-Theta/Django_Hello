# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    '''
    Model fields 可為 Django Model 定義不同型態的屬性。
    CharField -- 字串欄位，適合像 title、location 這種有長度限制的字串。
    TextField -- 合放大量文字的欄位
    URLField -- URL 設計的欄位
    DateTimeField -- 日期與時間的欄位，使用時會轉成 Python datetime 型別。
    '''
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
