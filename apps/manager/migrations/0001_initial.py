# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-24 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='카테고리명')),
                ('name_ko', models.CharField(max_length=32, null=True, unique=True, verbose_name='카테고리명')),
                ('name_en', models.CharField(max_length=32, null=True, unique=True, verbose_name='카테고리명')),
                ('is_open', models.BooleanField(default=True, verbose_name='사이트맵 노출여부')),
            ],
            options={
                'verbose_name': '카테고리',
                'verbose_name_plural': '카테고리(들)',
                'ordering': ['is_open'],
            },
        ),
        migrations.CreateModel(
            name='GroupServicePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField(choices=[(0, '권한없음'), (1, '접근권한'), (2, '읽기권한 (혹은 이에 준하는 특수권한)'), (3, '댓글권한 (혹은 이에 준하는 특수권한)'), (4, '쓰기권한 (혹은 이에 준하는 특수권한)'), (5, '수정권한 (혹은 이에 준하는 특수권한)'), (6, '삭제권한 (혹은 이에 준하는 특수권한)')], default=1, verbose_name='권한')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='그룹')),
            ],
            options={
                'verbose_name': '그룹별 서비스 이용권한',
                'verbose_name_plural': '그룹별 서비스 이용권한(들)',
                'ordering': ['service', 'permission', 'group'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='서비스명')),
                ('name_ko', models.CharField(max_length=32, null=True, unique=True, verbose_name='서비스명')),
                ('name_en', models.CharField(max_length=32, null=True, unique=True, verbose_name='서비스명')),
                ('url', models.CharField(default='/', help_text='도메인 하위 경로만 적어주세요. /aaa/bbb 형식을 지켜주세요.', max_length=32, verbose_name='서비스 최상위 주소')),
                ('level', models.IntegerField(default=1, help_text='같은 카테고리 내 서비스 간의 노출순서', verbose_name='노출순서')),
                ('description', models.TextField(blank=True, verbose_name='서비스 설명')),
                ('is_closed', models.BooleanField(default=False, help_text='설정 시 관리자를 제외한 모든 유저의 접속이 불가능합니다.', verbose_name='서비스 중지여부')),
                ('max_permission_anon', models.IntegerField(choices=[(0, '권한없음'), (1, '접근권한'), (2, '읽기권한 (혹은 이에 준하는 특수권한)'), (3, '댓글권한 (혹은 이에 준하는 특수권한)'), (4, '쓰기권한 (혹은 이에 준하는 특수권한)'), (5, '수정권한 (혹은 이에 준하는 특수권한)'), (6, '삭제권한 (혹은 이에 준하는 특수권한)')], default=0, verbose_name='비로그인 유저의 최대 권한')),
                ('max_permission_auth', models.IntegerField(choices=[(0, '권한없음'), (1, '접근권한'), (2, '읽기권한 (혹은 이에 준하는 특수권한)'), (3, '댓글권한 (혹은 이에 준하는 특수권한)'), (4, '쓰기권한 (혹은 이에 준하는 특수권한)'), (5, '수정권한 (혹은 이에 준하는 특수권한)'), (6, '삭제권한 (혹은 이에 준하는 특수권한)')], default=2, verbose_name='로그인 유저의 최대 권한')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Category', verbose_name='서비스가 속한 카테고리')),
                ('permitted_groups', models.ManyToManyField(related_name='permitted_services', through='manager.GroupServicePermission', to='auth.Group', verbose_name='그룹별 권한')),
            ],
            options={
                'verbose_name': '서비스',
                'verbose_name_plural': '서비스(들)',
                'ordering': ['category', 'level'],
            },
        ),
        migrations.AddField(
            model_name='groupservicepermission',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Service', verbose_name='서비스'),
        ),
    ]