# Generated by Django 4.0.6 on 2022-08-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0002_broker_loctions_delete_sentreceive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker_loctions',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]