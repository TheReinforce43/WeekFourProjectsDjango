# Generated by Django 5.0 on 2023-12-26 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskCategory', '0002_remove_category_task'),
        ('TaskModel', '0002_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TaskCategory.category'),
        ),
    ]
