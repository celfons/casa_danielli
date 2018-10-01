from django.contrib import admin
from .models import Paciente
from .models import Acompanhamento
from django import forms
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

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

    Atendimento = (
        (1,'QUIMIOTERAPIA'),
        (2,'RADIOTERAPIA'),
        (3,'CIRURGIA'),
        (4,'EXAMES'),
        (5,'OUTROS'),
    )

    ZONA = (
        (1,'URBANA'),
        (2,'RURAL'),
    )

    cor = forms.ChoiceField(choices=COR)    
    sexo = forms.ChoiceField(choices=SEXO)    
    estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL)    
    estado = forms.ChoiceField(choices=ESTADO)  
    atendimento = forms.ChoiceField(choices=Atendimento)  
    zona = forms.ChoiceField(choices=ZONA)  

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

class AcompanhamentoForm(forms.ModelForm):
    AC_AP = (
        (1,'PACIENTE'),
        (2,'ACOMPANHANTE'),
    )

    ac_ap = forms.ChoiceField(choices=AC_AP)  


class AcompanhamentoAdmin(admin.ModelAdmin):
    search_fields = ['paciente__nome', 'paciente__cidade']
    list_display = ['paciente', 'cidade', 'inclusao', 'saida']
    ordering = ['inclusao']
    autocomplete_fields = ['paciente']
    form = AcompanhamentoForm

    def cidade(self, obj):
        return obj.paciente.cidade

    def generate_pdf(self, request, obj):

        censo = []

        count = 0
        cafe_manha = 0
        while(count < len(obj)):
            if (obj[count].cafe_manha == 1):
                cafe_manha+=1
            count +=1

        censo.append({"cafe_manha":cafe_manha})

        count = 0
        almoco = 0
        while(count < len(obj)):
            if (obj[count].almoco == 1):
                almoco+=1
            count +=1

        censo.append({"almoco":almoco})

        count = 0
        cafe_tarde = 0
        while(count < len(obj)):
            if (obj[count].cafe_tarde == 1):
                cafe_tarde+=1
            count +=1

        censo.append({"cafe_tarde":cafe_tarde})

        count = 0
        banho = 0
        while(count < len(obj)):
            if (obj[count].banho == 1):
                banho+=1
            count +=1

        censo.append({"banho":banho})
    
        count = 0
        janta = 0
        while(count < len(obj)):
            if (obj[count].janta == 1):
                janta+=1
            count +=1

        censo.append({"janta":janta})

        count = 0
        hospedagem = 0
        while(count < len(obj)):
            if (obj[count].hospedagem == 1):
                hospedagem+=1
            count +=1

        censo.append({"hospedagem":hospedagem})

        context = {
            'obj': obj,
            'censo': censo[0]
        }

        html_string = render_to_string('reports/pdf_template.html', context)

        html = HTML(string=html_string, base_url=request.build_absolute_uri())

        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.short_description = "Download de Relatório"

    actions = [generate_pdf]

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Acompanhamento, AcompanhamentoAdmin)

	