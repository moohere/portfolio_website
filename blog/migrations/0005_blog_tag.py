# Generated by Django 2.1 on 2018-08-31 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180827_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(default='text', max_length=200),
            preserve_default=False,
        ),
    ]