# Generated by Django 4.0.4 on 2022-05-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_ordermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='state',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
