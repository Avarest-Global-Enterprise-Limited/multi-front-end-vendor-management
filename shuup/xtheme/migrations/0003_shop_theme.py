# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-28 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0033_order_modified_date'),
        ('shuup_xtheme', '0002_md_to_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedviewconfig',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved_views_config', to='shuup.Shop'),
        ),
        migrations.AddField(
            model_name='themesettings',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='themes_settings', to='shuup.Shop'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='theme_identifier',
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='themesettings',
            unique_together=set([('theme_identifier', 'shop')]),
        ),
    ]
