# Generated by Django 3.1.7 on 2021-02-28 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20210228_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auser',
            name='name',
        ),
        migrations.AddField(
            model_name='auser',
            name='username',
            field=models.CharField(blank=True, max_length=30, unique=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='auser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]