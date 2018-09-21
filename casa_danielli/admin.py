from django.contrib import admin
from .models import Paciente
from .models import Acompanhamento
from django import forms

class PacienteInline(admin.TabularInline):
    model = Paciente.cia.through
    fk_name = 'from_paciente' 
    fields = ('to_paciente',)
    autocomplete_fields = ['to_paciente']
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
        ('AC','AC'),
        ('AL','AL'),
        ('AP','AP'),
        ('AM','AM'),
        ('BA','BA'),
        ('CE','CE'),
        ('DF','DF'),
        ('ES','ES'),
        ('GO','GO'),
        ('MA','MA'),
        ('MT','MT'),
        ('MS','MS'),
        ('MG','MG'),
        ('PA','PA'),
        ('PB','PB'),
        ('PR','PR'),
        ('PE','PE'),
        ('PI','PI'),
        ('RJ','RJ'),
        ('RN','RN'),
        ('RS','RS'),
        ('RO','RO'),
        ('RR','RR'),
        ('SC','SC'),
        ('SP','SP'),
        ('SE','SE'),
        ('TO','TO'),
    )

    cor = forms.ChoiceField(choices=COR)    
    sexo = forms.ChoiceField(choices=SEXO)    
    estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL)    
    estado = forms.ChoiceField(choices=ESTADO)  

def checkout(modeladmin, request, queryset):
    queryset.update(hospedado=False)
checkout.short_description = "Checkout da Hospedagem"

def checkin(modeladmin, request, queryset):
    queryset.update(hospedado=True)
checkin.short_description = "Checkin da Hospedagem"

class PacienteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'prontuario', 'cpf']
    list_display = ['nome','prontuario', 'cpf', 'telefone','naturalidade', 'hospedado']
    inlines = [
        PacienteInline,
    ]
    form = PacienteForm
    actions = [checkout, checkin]

class AcompanhamentoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['nome', 'inclusao', 'atualizacao']
    ordering = ['inclusao']
    autocomplete_fields = ['nome']

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Acompanhamento, AcompanhamentoAdmin)

	