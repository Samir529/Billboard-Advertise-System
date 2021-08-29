# Generated by Django 2.2.17 on 2021-08-29 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard_Advertisement', '0002_auto_20210828_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentpriceupdate',
            old_name='current_price',
            new_name='max_price',
        ),
        migrations.AddField(
            model_name='currentpriceupdate',
            name='min_price',
            field=models.FloatField(default='0', max_length=10000),
        ),
        migrations.AlterField(
            model_name='postadvertisetable',
            name='location',
            field=models.CharField(choices=[('Dhaka', 'Dhaka'), ('Narayanganj', 'Narayanganj'), ('Gazipur', 'Gazipur'), ('Cumilla', 'Cumilla'), ('Chittagong', 'Chittagong'), ('Noakhali', 'Noakhali'), ('Jessore', 'Jessore'), ('Khulna', 'Khulna'), ('Barisal', 'Barisal'), ('Rajshahi', 'Rajshahi'), ('Sylhet', 'Sylhet'), ('Rangpur', 'Rangpur'), ('Feni', 'Feni'), ('Pabna', 'Pabna'), ('Faridpur', 'Faridpur'), ('Dinajpur', 'Dinajpur'), ('Coxs Bazar', 'Coxs Bazar'), ('Bogra', 'Bogra'), ('Tangail', 'Tangail'), ('Patuakhali', 'Patuakhali'), ('Lalmonirhat', 'Lalmonirhat'), ('Madaripur', 'Madaripur'), ('Naogaon', 'Naogaon'), ('Rajbari', 'Rajbari'), ('Narail', 'Narail'), ('Pirojpur', 'Pirojpur'), ('Sherpur', 'Sherpur'), ('Mars', 'Mars')], default='', max_length=30),
        ),
    ]
