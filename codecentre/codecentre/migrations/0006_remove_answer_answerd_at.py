# Generated by Django 2.1.1 on 2018-09-16 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coders_answers', '0005_auto_20180916_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answerd_at',
        ),
    ]
