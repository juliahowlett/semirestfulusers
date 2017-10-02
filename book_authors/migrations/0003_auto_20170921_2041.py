# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_authors_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books_authors',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='books_authors',
            name='book_id',
        ),
        migrations.AddField(
            model_name='authors',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_authors.Books'),
        ),
        migrations.DeleteModel(
            name='books_authors',
        ),
    ]