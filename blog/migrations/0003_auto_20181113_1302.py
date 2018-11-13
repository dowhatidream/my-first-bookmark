# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-13 04:02
from __future__ import unicode_literals

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=tagging.fields.TagField(blank=True, help_text='게시글에 대한 태그', max_length=255, verbose_name='태그'),
        ),
    ]