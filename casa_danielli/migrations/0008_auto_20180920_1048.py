# Generated by Django 2.2.dev20180920131230 on 2018-09-20 13:48

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('casa_danielli', '0007_auto_20180920_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acompanhamento',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='usuario',
        ),
        migrations.AddField(
            model_name='acompanhamento',
            name='usario',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paciente',
            name='usario',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
