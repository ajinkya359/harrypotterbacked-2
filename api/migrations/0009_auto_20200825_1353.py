# Generated by Django 3.1 on 2020-08-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200825_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='status',
        ),
        migrations.AddField(
            model_name='blogs',
            name='public',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
