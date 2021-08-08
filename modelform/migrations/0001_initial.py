# Generated by Django 3.2.6 on 2021-08-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=255)),
                ('enrollment', models.IntegerField(blank=True, null=True)),
                ('faculty', models.CharField(default='None', max_length=255)),
                ('year', models.CharField(choices=[('None', 'None'), ('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('forth', 'Forth')], default='None', max_length=255)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
