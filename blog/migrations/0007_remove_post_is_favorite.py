# Generated by Django 3.0 on 2019-12-17 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_favorite',
        ),
    ]
