# Generated by Django 3.0.6 on 2020-05-21 09:40

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_owner_mo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='mo',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
