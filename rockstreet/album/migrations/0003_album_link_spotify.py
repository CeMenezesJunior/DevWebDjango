# Generated by Django 3.0.2 on 2021-03-31 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20210329_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='link_spotify',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
