# Generated by Django 3.2.6 on 2021-08-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0002_auto_20210809_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRecord1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('customer_id', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='customer_address',
        ),
    ]
