# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

def return_date_time():
    return timezone.now()

class Paciente(models.Model):

    nome = models.CharField(max_length=255, blank=True, null=True)
    cia = models.ManyToManyField('self', blank=True, symmetrical=False, through='Relacionamento')
    prontuario = models.IntegerField(blank=True, null=True)
    atendimento = models.IntegerField(blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)
    estado_civil = models.IntegerField(blank=True, null=True)
    cor = models.IntegerField(blank=True, null=True)
    naturalidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    instrucao = models.CharField(max_length=50, blank=True, null=True)
    profissao = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(max_length=15, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    cns = models.CharField(max_length=30, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    trabalho = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    ibge = models.IntegerField(blank=True, null=True)
    mae = models.CharField(max_length=255, blank=True, null=True)
    pai = models.CharField(max_length=255, blank=True, null=True)
    convenio = models.CharField(max_length=255, blank=True, null=True)
    matricula = models.IntegerField(blank=True, null=True)
    validade = models.DateField(blank=True, null=True, default=return_date_time)
    inclusao = models.DateTimeField(blank=True, null=True, default=return_date_time)
    atualizacao = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True, null=True)
    hospedado = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'paciente'

    def __str__(self):
        return self.nome


class Relacionamento(models.Model):
    from_paciente = models.ForeignKey(Paciente, related_name='acompanhado', on_delete=models.CASCADE)
    to_paciente = models.ForeignKey(Paciente, related_name='acompanhante', on_delete=models.CASCADE)


class Acompanhamento(models.Model):

    ac_ap = models.CharField(max_length=255, blank=True, null=True)
    nome = models.ManyToManyField(Paciente, related_name='Acolhidos')
    hospital = models.CharField(max_length=255, blank=True, null=True)
    cafe_manha = models.BooleanField(default=False)
    almoco = models.BooleanField(default=False)
    cafe_tarde = models.BooleanField(default=False)
    banho = models.BooleanField(default=False)
    janta = models.BooleanField(default=False)
    hospedagem = models.CharField(max_length=255, blank=True, null=True)
    inclusao = models.DateTimeField(blank=True, null=True, default=return_date_time)
    atualizacao = models.DateTimeField(blank=True, null=True, default=return_date_time)
    ativo = models.BooleanField(default=False)
    usuario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'acompanhamento'

class Acolhidos(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    acompanhamento = models.ForeignKey(Acompanhamento, on_delete=models.CASCADE)


