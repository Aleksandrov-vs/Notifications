# Generated by Django 3.0.6 on 2020-05-19 01:34

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('price', models.FloatField(blank=True, default=5.0, editable=False)),
                ('file', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage('media/files'), upload_to='')),
                ('text', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=20)),
                ('time', models.DateTimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
            ],
        ),
    ]
