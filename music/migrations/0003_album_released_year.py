# Generated by Django 2.0.6 on 2018-06-15 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='released_year',
            field=models.CharField(default='-', max_length=5),
        ),
    ]
