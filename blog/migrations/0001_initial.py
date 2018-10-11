# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-11 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('slug', models.SlugField(allow_unicode=True, help_text='제목에 대한 한 단어의 별명.', unique=True, verbose_name='슬러그')),
                ('description', models.CharField(blank=True, help_text='간략한 설명 문구.', max_length=100, verbose_name='설명')),
                ('content', models.TextField(verbose_name='내용')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='최초 생성 일시')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='최종 수정 일시')),
            ],
            options={
                'verbose_name': '기사',
                'verbose_name_plural': '기사 모음',
                'db_table': 'my_posts',
                'ordering': ('-modify_date',),
            },
        ),
    ]
