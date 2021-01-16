# Generated by Django 3.0.3 on 2020-02-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200227_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumncsv',
            name='Account_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user_information',
            name='First_name',
            field=models.CharField(default='-', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user_stats',
            name='Email',
            field=models.EmailField(max_length=60, unique=True),
        ),
    ]
