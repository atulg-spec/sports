# Generated by Django 4.2.7 on 2024-12-31 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_game_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='instructions',
            field=models.TextField(default=''),
        ),
    ]