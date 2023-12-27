# Generated by Django 5.0 on 2023-12-26 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskCategory', '0002_remove_category_task'),
        ('TaskModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='TaskCategory.category'),
        ),
    ]
