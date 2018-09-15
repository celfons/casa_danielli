from django.contrib import admin
from .models import Paciente
from django import forms

class PacienteInline(admin.TabularInline):
    model = Paciente.cia.through
    fk_name = 'from_paciente' 
    fields = ('to_paciente',)
    show_change_link = True
    extra = 1
    verbose_name = "Acompanhante"
    verbose_name_plural = "Acompanhantes"

class PacienteForm(forms.ModelForm):
    COR = (
        (1,'BRANCO'),
        (2,'AMARELO'),
        (3,'PARDO'),
        (4,'PRETO'),
        (5,'DESCONHECIDO'),
    )

    SEXO = (
        (1,'MASCULINO'),
        (2,'FEMININO'),
        (3,'NAO INFORMADO'),
    )

    ESTADO_CIVIL = (
        (1,'SOLTEIRO(A)'),
        (2,'CASADO(A)'),
        (3,'SEPARADO(A)'),
        (4,'VIUVO(A)'),
        (5,'DESCONHECIDO'),
    )

    ESTADO = (
        ('Acre','AC'),
        ('Alagoas','AL'),
        ('Amapá','AP'),
        ('Amazonas','AM'),
        ('Bahia','BA'),
        ('Ceará','CE'),
        ('Distrito Federal','DF'),
        ('Espírito Santo','ES'),
        ('Goiás','GO'),
        ('Maranhão','MA'),
        ('Mato Grosso','MT'),
        ('Mato Grosso do Sul','MS'),
        ('Minas Gerais','MG'),
        ('Pará','PA'),
        ('Paraíba','PB'),
        ('Paraná','PR'),
        ('Pernambuco','PE'),
        ('Piauí','PI'),
        ('Rio de Janeiro','RJ'),
        ('Rio Grande do Norte','RN'),
        ('Rio Grande do Sul','RS'),
        ('Rondônia','RO'),
        ('Roraima','RR'),
        ('Santa Catarina','SC'),
        ('São Paulo','SP'),
        ('Sergipe','SE'),
        ('Tocantins','TO'),
    )

    cor = forms.ChoiceField(choices=COR)    
    sexo = forms.ChoiceField(choices=SEXO)    
    estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL)    
    estado = forms.ChoiceField(choices=ESTADO)  

class PacienteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'prontuario', 'cpf']
    list_display = ('nome','prontuario', 'cpf', 'telefone','naturalidade')
    inlines = [
        PacienteInline,
    ]
    form = PacienteForm

admin.site.register(Paciente, PacienteAdmin)
	