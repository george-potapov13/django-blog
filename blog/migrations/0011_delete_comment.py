# Generated by Django 3.0 on 2019-12-18 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_delete_favorite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
