# Generated by Django 4.1.5 on 2023-01-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='sickness',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='text',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
    ]
