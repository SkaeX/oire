# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0001_initial'),
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluations.Evaluation')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.IntegerField(default=0)),
                ('two', models.IntegerField(default=0)),
                ('three', models.IntegerField(default=0)),
                ('four', models.IntegerField(default=0)),
                ('five', models.IntegerField(default=0)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluations.Evaluation')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluations.Question')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.Section')),
            ],
        ),
    ]
