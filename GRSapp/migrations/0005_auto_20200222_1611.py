# Generated by Django 3.0 on 2020-02-22 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRSapp', '0004_auto_20200222_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='suggts',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]