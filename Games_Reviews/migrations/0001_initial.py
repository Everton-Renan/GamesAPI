# Generated by Django 5.1.2 on 2024-10-30 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('reviews', models.PositiveIntegerField()),
                ('developer', models.CharField()),
                ('publisher', models.CharField()),
                ('series', models.CharField()),
                ('platforms', models.CharField()),
                ('release', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=50)),
                ('review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Games_Reviews.review')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Games_Reviews.review')),
            ],
        ),
    ]
