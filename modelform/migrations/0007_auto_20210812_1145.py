# Generated by Django 3.2.6 on 2021-08-12 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0006_customerrecord_items'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerrecord',
            options={'verbose_name_plural': 'Customer Records'},
        ),
        migrations.AlterModelOptions(
            name='customerrecord1',
            options={'verbose_name_plural': 'Customer Records1'},
        ),
        migrations.AlterModelOptions(
            name='studentrecord',
            options={'verbose_name_plural': 'Student Records'},
        ),
    ]