# Generated by Django 2.2.17 on 2021-09-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard_Advertisement', '0009_auto_20210913_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirm_post',
            name='dealDuration',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
