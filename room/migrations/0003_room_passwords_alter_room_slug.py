# Generated by Django 4.2.8 on 2023-12-14 14:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='passwords',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
