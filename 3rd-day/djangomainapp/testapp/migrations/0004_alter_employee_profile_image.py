# Generated by Django 4.0.3 on 2022-04-01 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_employee_profile_image_alter_employee_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]