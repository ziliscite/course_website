# Generated by Django 5.0.3 on 2024-03-12 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_usercourse_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercourse',
            name='rating',
        ),
    ]
