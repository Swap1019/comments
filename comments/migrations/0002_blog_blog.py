# Generated by Django 5.0.7 on 2024-07-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog',
            field=models.TextField(default='hi', verbose_name='content'),
            preserve_default=False,
        ),
    ]
