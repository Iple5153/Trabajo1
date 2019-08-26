from django.contrib import admin
from django.contrib.admin import AdminSite
from Iple.Apps.GestionAcademica.models import *
from django.utils.translation import ugettext_lazy  
# Register your models here.
class AdminAlumno(admin.ModelAdmin):
	list_display = ['Id_Alu','Nom_Alu','Ape_Alu','Fna_Alu','Are_Alu','Edad']
	search_fields= ['Nom_Alu','Ape_Alu']
	fields=[('Nom_Alu','Ape_Alu','Dir_Alu','Nac_Alu','Sex_Alu'),('Are_Alu','Fna_Alu','Cpr_Alu'),('Tfi_Alu','Tmo_Alu','Mod_Alu','Cor_Alu','Tsa_Alu','Tutore'),('Doc_Alu')]
#	fields=[('Nom_Alu','Ape_Alu','Dir_Alu','Nac_Alu','Sex_Alu'),('Are_Alu','Fna_Alu','Cpr_Alu'),('Tfi_Alu','Doc_Alu','Tmo_Alu','Mod_Alu','Tutore','Cor_Alu','Tsa_Alu')]
	class Meta:
		model = Alumno

class AdminAsignatura(admin.ModelAdmin):
	list_display = ['Id_Asi','Nom_Asi','Cho_Asi','Dpt_Asi','Tip_Asi']
	search_fields= ['Id_Asi']
	fields=[('Id_Asi', 'Nom_Asi'),('Cho_Asi','Dpt_Asi','Tip_Asi')]
	class Meta:
		model = Asignatura

class AdminGrado(admin.ModelAdmin):
	list_display = ['Id_Gra','Empleado']
	search_fields= ['Id_Gra']
	fields=[('Id_Gra', 'Empleado'),('Asi01','Asi02'),('Asi03','Asi04'),('Asi05','Asi06'),('Asi07','Asi08'),('Asi09','Asi10'),('Asi11','Asi12'),('Asi13','Asi14'),('Asi15','Asi16')]
	class Meta:
		model = Grado

class AdminEmpleado(admin.ModelAdmin):
	list_display = ['Id_Emp','Nom_Emp','Sex_Emp','Fna_Emp','Dpt_Emp','Tip_Emp','Car_Emp']
	search_fields= ['Nom_Emp']
	fields=[('Nom_Emp','Dir_Emp','Sex_Emp'),('Nac_Emp','Dpt_Emp','Tip_Emp'),('Cor_Emp','Fna_Emp','Tfi_Emp','Tmo_Emp','Tsa_Emp','Car_Emp')]
	class Meta:
		model = Empleado

class AdminTutore(admin.ModelAdmin):
	list_display = ['Id_Tut','Nom_Tut','Dir_Tut','Sex_Tut','Ced_Tut','Tfi_Tut']
	search_fields= ['Nom_Tut']
	fields=[('Nom_Tut','Dir_Tut','Sex_Tut'),('Fna_Tut','Ced_Tut'),('Tfi_Tut','Tmo_Tut')]
	class Meta:
		model = Tutore

admin.site.register(Alumno,AdminAlumno)
admin.site.register(Empleado,AdminEmpleado)
admin.site.register(Asignatura,AdminAsignatura)
admin.site.register(Grado,AdminGrado)
admin.site.register(Tutore,AdminTutore)

