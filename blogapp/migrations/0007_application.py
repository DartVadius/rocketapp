# Generated by Django 2.0.5 on 2018-06-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20180608_0629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_name', models.CharField(blank=True, max_length=255)),
                ('admin_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
