# Generated by Django 2.1.1 on 2018-09-16 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coders_answerQuestion', '0002_auto_20180916_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeringthequestion',
            name='answerRequestedIn',
            field=models.CharField(choices=[('1', 'Pyhton'), ('2', 'Java'), ('3', 'JavaScript'), ('4', 'c++')], default='', max_length=1),
        ),
    ]
