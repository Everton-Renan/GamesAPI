# Generated by Django 5.1.2 on 2024-11-03 18:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Games_Reviews', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='GenerateKeys',
        ),
    ]