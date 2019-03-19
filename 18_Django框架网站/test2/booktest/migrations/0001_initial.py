# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('atitle', models.CharField(max_length=30)),
                ('aParent', models.ForeignKey(blank='True', null=True, to='booktest.AreaInfo')),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'booktest_bookinfo',
            },
        ),
        migrations.CreateModel(
            name='EmployeeBasicInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=False)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('addr', models.CharField(max_length=256)),
                ('employee_basic', models.OneToOneField(to='booktest.EmployeeBasicInfo')),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=False)),
                ('hcomment', models.CharField(max_length=128)),
                ('is_delete', models.BooleanField(default=False)),
                ('hbook', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type_name', models.CharField(max_length=20)),
                ('type_news', models.ManyToManyField(to='booktest.NewsInfo')),
            ],
        ),
        migrations.AddField(
            model_name='newsinfo',
            name='new_type',
            field=models.ManyToManyField(to='booktest.NewsType'),
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='employee_data',
            field=models.OneToOneField(to='booktest.EmployeeDetailInfo'),
        ),
    ]
