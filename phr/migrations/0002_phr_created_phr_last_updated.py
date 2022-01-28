# Generated by Django 4.0.1 on 2022-01-28 00:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('phr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phr',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phr',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]