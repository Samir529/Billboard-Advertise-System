# Generated by Django 2.2.17 on 2021-09-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard_Advertisement', '0013_auto_20210913_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirm_post',
            name='dealDuration',
            field=models.DateField(default=None),
        ),
    ]
