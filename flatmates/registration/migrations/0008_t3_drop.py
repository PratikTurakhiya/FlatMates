# Generated by Django 3.0.6 on 2020-05-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20200518_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='t3',
            name='drop',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
