# Generated by Django 4.0.4 on 2022-05-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_ordermodel_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]