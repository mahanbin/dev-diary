# Generated by Django 2.0.13 on 2019-11-30 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diaryboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='content',
        ),
    ]
