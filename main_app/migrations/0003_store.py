# Generated by Django 3.1.6 on 2021-04-02 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210329_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=60)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.drink')),
            ],
        ),
    ]
