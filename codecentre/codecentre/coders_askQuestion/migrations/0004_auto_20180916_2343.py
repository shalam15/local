# Generated by Django 2.1.1 on 2018-09-16 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coders_askQuestion', '0003_auto_20180916_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeringthequestion',
            name='theQuestion',
            field=models.TextField(default=(('1', 'The Question Goes Here'),), max_length=10000),
        ),
    ]