from django.contrib import admin
from django.contrib.admin import AdminSite
#from Iple.Apps.GestioAcademica.models import *
from Iple.Apps.Transacciones.models import *
# Register your models here.

class AdminNota(admin.ModelAdmin):
	list_display = ('Lec_Not','Asignatura','Grado','Alumno','Nt1_Not','Nt2_Not','Nt3_Not','Nt4_Not','Pfi_Not','Pco_Not','Pex_Not')
	search_fields= ['Alumno__Nom_Alu']
	fields=[('Lec_Not','Asignatura','Grado','Alumno'),('Nt1_Not','Nt2_Not','Nt3_Not','Nt4_Not','Pfi_Not','Pco_Not','Pex_Not')]
	class Meta:
		model = Nota
		unique_together = [("Lec_Not", "Asignatura", "Grado", "Alumno")]

class AdminCobro(admin.ModelAdmin):
	list_display = ('Nco_Cob','Fco_Cob','Mco_Cob','Con_Cob')
	search_fields= ['Nco_Cob','Fco_Cob']
	fields=[('Fco_Cob','Mco_Cob','Con_Cob')]
	class Meta:
		model = Cobro

class AdminPsicologia(admin.ModelAdmin):
	list_display = ('Nre_Psi','Tre_Psi','Fre_Psi','Grado','Alumno','Empleado','Mre_Psi','Rec_Psi')
	search_fields= ['Alumno']
	fields=[('Tre_Psi','Fre_Psi','Grado','Alumno','Empleado'),('Mre_Psi','Rec_Psi')]
	class Meta:
		model = Psicologia
admin.site.register(Nota,AdminNota)
admin.site.register(Cobro,AdminCobro)
admin.site.register(Psicologia,AdminPsicologia)
