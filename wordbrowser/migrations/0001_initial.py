# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('article', models.IntegerField(max_length=3)),
                ('part_of_speech', models.CharField(max_length=50)),
                ('meaning', models.CharField(max_length=100)),
                ('extra', models.CharField(max_length=100)),
            ],
        ),
    ]
