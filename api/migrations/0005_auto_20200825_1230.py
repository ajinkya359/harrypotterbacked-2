# Generated by Django 3.1 on 2020-08-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_group_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='token',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
