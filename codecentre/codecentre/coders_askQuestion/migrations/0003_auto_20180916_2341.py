# Generated by Django 2.1.1 on 2018-09-16 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coders_askQuestion', '0002_auto_20180916_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeringthequestion',
            name='theQuestion',
            field=models.CharField(choices=[('1', 'The Question Goes Here')], default='', max_length=30),
        ),
        migrations.AddField(
            model_name='answeringthequestion',
            name='whoAsked',
            field=models.CharField(choices=[('1', 'shalam15'), ('2', 'ajayiabdulsalam')], default='', max_length=1),
        ),
    ]
