# Generated by Django 4.0.2 on 2022-02-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_student_options_student_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]