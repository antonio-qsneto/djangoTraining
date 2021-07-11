from django.contrib import admin
from .models import CPF, Departamento, Empregado, Telefone

admin.site.register(Departamento)
admin.site.register(Empregado)
admin.site.register(Telefone)
admin.site.register(CPF)