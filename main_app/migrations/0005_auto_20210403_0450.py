# Generated by Django 3.1.6 on 2021-04-03 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210402_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drinker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='pouring',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='drink',
            name='drinker',
            field=models.ManyToManyField(to='main_app.Drinker'),
        ),
    ]
