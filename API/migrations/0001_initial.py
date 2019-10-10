# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-30 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apaterno', models.CharField(max_length=50)),
                ('amaterno', models.CharField(max_length=50)),
                ('fechanac', models.DateField()),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
