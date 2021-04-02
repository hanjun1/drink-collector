# Generated by Django 3.1.6 on 2021-04-02 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pouring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pour', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='drink',
            name='size',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Store',
        ),
        migrations.AddField(
            model_name='pouring',
            name='drink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.drink'),
        ),
    ]
