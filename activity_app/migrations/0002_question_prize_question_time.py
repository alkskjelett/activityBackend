# Generated by Django 4.0.3 on 2022-04-05 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='prize',
            field=models.IntegerField(blank=True, default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='time',
            field=models.IntegerField(blank=True, default=3),
            preserve_default=False,
        ),
    ]