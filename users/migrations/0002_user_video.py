# Generated by Django 3.0.6 on 2020-11-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='video',
            field=models.FileField(default=False, upload_to='user_media', verbose_name='../media'),
        ),
    ]
