# Generated by Django 2.2.2 on 2019-06-24 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Announcement',
        ),
        migrations.DeleteModel(
            name='Timeline',
        ),
    ]
