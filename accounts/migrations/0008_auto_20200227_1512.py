# Generated by Django 3.0.3 on 2020-02-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alumncsv_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumncsv',
            name='Codigo_Alumn_USB',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='First_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Last_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Mailing_city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Mailing_country',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Mailing_state',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Middle_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Mobile',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Workplace',
            field=models.CharField(max_length=40),
        ),
    ]