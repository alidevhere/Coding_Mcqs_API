# Generated by Django 3.1.7 on 2021-05-08 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding_api', '0003_auto_20210509_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcq',
            name='options',
            field=models.CharField(default='default options', max_length=256),
        ),
        migrations.DeleteModel(
            name='options',
        ),
    ]
