# Generated by Django 2.2.dev20180828184008 on 2018-09-15 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('prontuario', models.IntegerField(blank=True, null=True)),
                ('atendimento', models.IntegerField(blank=True, null=True)),
                ('nascimento', models.DateField(blank=True, null=True)),
                ('sexo', models.IntegerField(blank=True, null=True)),
                ('estado_civil', models.IntegerField(blank=True, null=True)),
                ('cor', models.IntegerField(blank=True, null=True)),
                ('naturalidade', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=2, null=True)),
                ('instrucao', models.CharField(blank=True, max_length=50, null=True)),
                ('profissao', models.CharField(blank=True, max_length=50, null=True)),
                ('cpf', models.CharField(blank=True, max_length=15, null=True)),
                ('rg', models.CharField(blank=True, max_length=15, null=True)),
                ('cns', models.CharField(blank=True, max_length=30, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('trabalho', models.CharField(blank=True, max_length=50, null=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('cidade', models.CharField(blank=True, max_length=255, null=True)),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('ibge', models.IntegerField(blank=True, null=True)),
                ('mae', models.CharField(blank=True, max_length=255, null=True)),
                ('pai', models.CharField(blank=True, max_length=255, null=True)),
                ('convenio', models.CharField(blank=True, max_length=255, null=True)),
                ('matricula', models.IntegerField(blank=True, null=True)),
                ('validade', models.DateField(blank=True, null=True)),
                ('inclusao', models.DateTimeField(blank=True, null=True)),
                ('atualizacao', models.DateTimeField(blank=True, null=True)),
                ('usuario', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'paciente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Relacionamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompanhado', to='casa_danielli.Paciente')),
                ('to_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompanhante', to='casa_danielli.Paciente')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='cia',
            field=models.ManyToManyField(blank=True, through='casa_danielli.Relacionamento', to='casa_danielli.Paciente'),
        ),
    ]
