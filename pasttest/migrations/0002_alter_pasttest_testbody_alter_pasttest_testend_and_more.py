# Generated by Django 4.0 on 2021-12-21 21:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pasttest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasttest',
            name='testbody',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='pasttest',
            name='testend',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pasttest',
            name='testimg',
            field=models.ImageField(default='', upload_to='pasttestmedia/projimage/'),
        ),
        migrations.AlterField(
            model_name='pasttest',
            name='testquotes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='pasttest',
            name='teststart',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pasttest',
            name='testtitle',
            field=models.CharField(default='', max_length=200),
        ),
    ]