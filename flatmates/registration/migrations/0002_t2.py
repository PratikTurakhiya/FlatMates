# Generated by Django 3.0.6 on 2020-05-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='t2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7)),
                ('pic', models.FileField(blank='true', null='true', upload_to='')),
            ],
        ),
    ]
