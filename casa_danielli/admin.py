from django.contrib import admin
from .models import Paciente

class PacienteInline(admin.TabularInline):
    model = Paciente.cia.through
    fk_name = 'from_paciente' 
    fields = ('to_paciente',)
    show_change_link = True
    extra = 1
    verbose_name = "Acompanhante"
    verbose_name_plural = "Acompanhantes"

class PacienteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'prontuario', 'cpf']
    list_display = ('nome','prontuario', 'cpf', 'telefone','naturalidade')
    inlines = [
        PacienteInline,
    ]

admin.site.register(Paciente, PacienteAdmin)
	