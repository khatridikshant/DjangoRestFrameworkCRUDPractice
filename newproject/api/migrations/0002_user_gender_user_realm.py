# Generated by Django 5.1.1 on 2024-09-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='unknown', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='realm',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]
