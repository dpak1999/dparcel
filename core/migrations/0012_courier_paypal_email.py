# Generated by Django 3.1.3 on 2022-03-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20220302_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='paypal_email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]