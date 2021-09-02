# Generated by Django 2.2.17 on 2021-08-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard_Advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirm_post',
            name='adCode',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='postadvertisetable',
            name='location',
            field=models.CharField(blank=True, choices=[('Dhaka', 'Dhaka'), ('Narayanganj', 'Narayanganj'), ('Gazipur', 'Gazipur'), ('Cumilla', 'Cumilla'), ('Chittagong', 'Chittagong'), ('Noakhali', 'Noakhali'), ('Jessore', 'Jessore'), ('Khulna', 'Khulna'), ('Barisal', 'Barisal'), ('Rajshahi', 'Rajshahi'), ('Sylhet', 'Sylhet'), ('Rangpur', 'Rangpur'), ('Feni', 'Feni'), ('Pabna', 'Pabna'), ('Faridpur', 'Faridpur'), ('Dinajpur', 'Dinajpur'), ('Coxs Bazar', 'Coxs Bazar'), ('Bogra', 'Bogra'), ('Tangail', 'Tangail'), ('Patuakhali', 'Patuakhali'), ('Lalmonirhat', 'Lalmonirhat'), ('Madaripur', 'Madaripur'), ('Naogaon', 'Naogaon'), ('Rajbari', 'Rajbari'), ('Narail', 'Narail'), ('Pirojpur', 'Pirojpur'), ('Sherpur', 'Sherpur'), ('Mars', 'Mars')], default='', max_length=30),
        ),
    ]