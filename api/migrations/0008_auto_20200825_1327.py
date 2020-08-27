# Generated by Django 3.1 on 2020-08-25 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200825_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='private_blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogid', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.blogs')),
                ('groupid', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.groups')),
            ],
        ),
        migrations.DeleteModel(
            name='blogs_to_groups',
        ),
    ]
