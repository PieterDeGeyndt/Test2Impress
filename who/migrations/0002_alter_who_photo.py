# Generated by Django 4.0 on 2021-12-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('who', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='who',
            name='Photo',
            field=models.ImageField(upload_to='whomedia/whoimage/'),
        ),
    ]