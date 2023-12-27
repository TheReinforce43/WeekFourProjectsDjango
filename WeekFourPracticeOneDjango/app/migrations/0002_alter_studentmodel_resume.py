# Generated by Django 5.0 on 2023-12-26 04:20

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='Resume',
            field=models.FileField(upload_to='', validators=[app.models.validate_file, django.core.validators.FileExtensionValidator(['pdf', 'docx'])]),
        ),
    ]
