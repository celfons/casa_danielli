# Generated by Django 2.2.dev20180924184437 on 2018-09-29 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casa_danielli', '0014_auto_20180929_0929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acompanhamento',
            old_name='nome',
            new_name='paciente',
        ),
    ]