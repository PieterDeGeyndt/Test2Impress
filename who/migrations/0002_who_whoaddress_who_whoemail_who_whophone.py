# Generated by Django 4.0 on 2022-01-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('who', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='who',
            name='whoaddress',
            field=models.TextField(default='', verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='who',
            name='whoemail',
            field=models.TextField(default='', verbose_name='e-mailaddress'),
        ),
        migrations.AddField(
            model_name='who',
            name='whophone',
            field=models.TextField(default='+32 (0) ', verbose_name='Tel nr'),
        ),
    ]
