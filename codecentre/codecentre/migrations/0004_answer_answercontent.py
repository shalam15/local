# Generated by Django 2.1.1 on 2018-09-16 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coders_answers', '0003_auto_20180916_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answerContent',
            field=models.TextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]