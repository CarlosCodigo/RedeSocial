# Generated by Django 3.2.8 on 2021-11-28 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario_prof', '0002_auto_20211127_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acesso',
            old_name='usuario',
            new_name='nome',
        ),
    ]
