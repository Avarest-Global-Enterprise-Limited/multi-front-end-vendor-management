# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-31 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_simple_cms', '0009_remove_page_page_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='render_title',
            field=models.BooleanField(default=True, help_text='Check this if this page should have a visible title', verbose_name='render title'),
        ),
        migrations.AddField(
            model_name='page',
            name='template_name',
            field=models.TextField(default='shuup/simple_cms/page.jinja', max_length=500, verbose_name='Template path'),
        ),
        migrations.AlterField(
            model_name='pagetranslation',
            name='content',
            field=models.TextField(help_text='The page content. This is the text that is displayed when customers click on your page link.You can leave this empty and add all page content through placeholder editor in shop front.To edit the style of the page you can use the Snippet plugin which is in shop front editor.', verbose_name='content'),
        ),
    ]
