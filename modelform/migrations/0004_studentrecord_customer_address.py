# Generated by Django 3.2.6 on 2021-08-11 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0003_auto_20210811_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrecord',
            name='customer_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modelform.customerrecord'),
        ),
    ]