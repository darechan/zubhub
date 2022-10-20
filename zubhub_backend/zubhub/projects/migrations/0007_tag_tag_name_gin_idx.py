# Generated by Django 3.2 on 2022-10-20 08:54

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20220409_1917'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tag',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name'], name='tag_name_gin_idx', opclasses=['gin_trgm_ops']),
        ),
    ]