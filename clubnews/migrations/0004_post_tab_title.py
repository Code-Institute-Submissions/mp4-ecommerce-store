# Generated by Django 3.0.8 on 2020-08-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubnews', '0003_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tab_title',
            field=models.CharField(default='Club News', max_length=255),
        ),
    ]
