# Generated by Django 3.1.3 on 2022-02-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_category_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pickeup_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='pickeup_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='pickeup_lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='pickeup_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='pickeup_phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
