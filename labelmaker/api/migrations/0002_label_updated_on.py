# Generated by Django 3.1.2 on 2020-10-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
