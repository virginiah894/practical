# Generated by Django 3.2.9 on 2021-12-05 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_stream_student_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stream',
            old_name='title',
            new_name='stream_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='title',
            new_name='stream_name',
        ),
    ]
