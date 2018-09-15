from django.contrib import admin
from .models import Paciente

class PacienteInline(admin.TabularInline):
    model = Paciente.cia.through 

class PacienteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'prontuario', 'cpf']
    list_display = ('nome','prontuario', 'cpf', 'telefone','naturalidade')
    inlines = [
        PacienteInline,
    ]

admin.site.register(Paciente, PacienteAdmin)
	