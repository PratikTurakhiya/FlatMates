# Generated by Django 3.0.6 on 2020-05-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20200518_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t3',
            name='pic',
            field=models.ImageField(blank='true', null='true', upload_to='images/'),
        ),
    ]
