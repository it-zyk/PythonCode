# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_heroinfo_is_delete'),
    ]

    operations = [
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
