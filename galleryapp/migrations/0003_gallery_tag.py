# Generated by Django 2.0.5 on 2018-06-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20180608_0629'),
        ('galleryapp', '0002_auto_20180612_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blogapp.Tag'),
        ),
    ]
