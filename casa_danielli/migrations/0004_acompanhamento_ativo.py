# Generated by Django 2.2.dev20180915135820 on 2018-09-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casa_danielli', '0003_auto_20180916_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='acompanhamento',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
    ]
