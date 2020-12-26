# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-22 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0063_add_related_name_for_staff_members'),
        ('campaigns', '0016_remove_hourcondition_validator'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildrenProductCondition',
            fields=[
                ('basketcondition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='campaigns.BasketCondition')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shuup.Product')),
            ],
            options={
                'manager_inheritance_from_future': True,
            },
            bases=('campaigns.basketcondition',),
        ),
    ]
