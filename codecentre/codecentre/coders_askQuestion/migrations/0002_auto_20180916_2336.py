# Generated by Django 2.1.1 on 2018-09-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coders_askQuestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='answeringTheQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answerWith', models.CharField(choices=[('1', 'Pyhton'), ('2', 'Java'), ('3', 'JavaScript'), ('4', 'c++')], default='', max_length=2)),
                ('theAnswers', models.TextField(default='', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='questionToBeAnswerd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whoAsked', models.CharField(choices=[('1', 'shalam15'), ('2', 'ajayiabdulsalam')], default='', max_length=1)),
                ('theQuestion', models.CharField(choices=[('1', 'The Question Goes Here')], default='', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
