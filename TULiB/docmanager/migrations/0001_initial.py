# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=14)),
                ('release_date', models.DateField()),
                ('doc_type', models.IntegerField(choices=[(0, 'Book'), (1, 'Thesis')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docmanager.Author')),
            ],
        ),
    ]