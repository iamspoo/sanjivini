
# Generated by Django 2.2.6 on 2020-01-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0002_auto_20200109_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='text',
            field=models.TextField(default='def'),
            preserve_default=False,
        ),
    ]
