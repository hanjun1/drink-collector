# Generated by Django 3.1.6 on 2021-03-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='size',
            field=models.CharField(max_length=100),
        ),
    ]
