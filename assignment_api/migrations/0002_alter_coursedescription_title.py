# Generated by Django 5.0.2 on 2024-11-26 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedescription',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CourseDesc', to='assignment_api.coursedetail'),
        ),
    ]
