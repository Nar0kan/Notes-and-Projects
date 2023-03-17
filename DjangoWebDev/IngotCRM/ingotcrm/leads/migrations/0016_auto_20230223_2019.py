# Generated by Django 3.1.4 on 2023-02-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0015_auto_20230204_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='lead<built-in function id>'),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='media/', verbose_name=models.CharField(max_length=200, unique=True)),
        ),
    ]