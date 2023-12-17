# Generated by Django 4.2.7 on 2023-12-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.TextField(default='Default Caption'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='post_images/'),
        ),
    ]