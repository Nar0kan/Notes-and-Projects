# Generated by Django 4.1.7 on 2023-03-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0026_agent_phone_number_agent_photo_agent_position_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='position',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, default='unknown', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/agents', verbose_name='Photo'),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, default='employee', max_length=100, null=True),
        ),
    ]
