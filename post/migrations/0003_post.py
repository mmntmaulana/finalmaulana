# Generated by Django 2.1.7 on 2019-02-25 05:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0002_auto_20190224_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False)),
                ('date_updated', models.DateTimeField(verbose_name='date updated')),
                ('content', models.TextField(max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]