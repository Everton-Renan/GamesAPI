# Generated by Django 5.1.2 on 2024-11-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games_Reviews', '0003_alter_generatekeys_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviews',
            field=models.PositiveIntegerField(),
        ),
    ]
