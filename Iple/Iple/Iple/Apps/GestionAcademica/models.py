from django.db import models
from Iple.Apps.GestionAcademica.models import *
from multiselectfield import MultiSelectField
from datetime  import datetime, date,timedelta
import calendar
# Create your models here.
class Tutore(models.Model):
	Id_Tut = models.AutoField('Identificación',primary_key=True)
	Nom_Tut = models.CharField('Nombre',max_length=30,blank=False,null=False)
	Dir_Tut = models.CharField('Dirección',max_length=40,blank=False,null=False)
	Nac_Tut = models.CharField('Nacionalidad',max_length=3,blank=True,null=True)
	Sex_SelT = (('F', 'Femenino'),('M', 'Masculino'))
	Sex_Tut = models.CharField('Sexo',max_length = 1, choices = Sex_SelT)
	Fna_Tut = models.DateField('Fecha de Nacimiento')
	Ced_Tut = models.CharField('Cédula',max_length=13,blank=True,null=True)
	Tfi_Tut = models.CharField('Teléfono Fijo',max_length=15,blank=True,null=True)
	Tmo_Tut = models.CharField('Teléfono Móvil',max_length=15,blank=True,null=True)
	
	def InfTutore(self):
		cTu = "{0}"
		return cTu.format (self.Nom_Tut)

	def __str__(self):
		return self.InfTutore()

class Alumno(models.Model):
	Id_Alu = models.AutoField('Identificación',primary_key=True)
	Ape_Alu = models.CharField('Apellidos',max_length=20,blank=False,null=False)
	Nom_Alu = models.CharField('Nombres',max_length=20,blank=False,null=False)
	Dir_Alu = models.CharField('Dirección',max_length=40,blank=False,null=False)
	Nac_Alu = models.CharField('Nacionalidad',max_length=3,blank=True,null=True)
	Cpr_Alu = models.CharField('Centro Procedencia',max_length=40)
	Con_Sel = (('A', 'Activo'),('S', 'Separado'))
	Con_Alu = models.CharField('Condición',max_length = 1, choices = Con_Sel)
	Sex_Sel = (('F', 'Femenino'),('M', 'Masculino'))
	Sex_Alu = models.CharField('Sexo',max_length = 1, choices = Sex_Sel)
	Fna_Alu = models.DateField('Fecha de Nacimiento')
	Cor_Alu = models.EmailField('Correo Electrónico',max_length=35,blank=True,null=True)
	Tfi_Alu = models.CharField('Teléfono Fijo',max_length=15,blank=True,null=True)
	Tmo_Alu = models.CharField('Teléfono Móvil',max_length=15,blank=True,null=True)
	Tsa_Alu = models.CharField('Tipo de Sangre',max_length=10,blank=True,null=True)
	Mod_Sel = (('G', 'General'),('T', 'Técnico'))
	Mod_Alu = models.CharField('Modalidad',max_length = 1, choices = Mod_Sel)
	Are_Sel = (('GAT', 'Gestión Adminidtrativa y Tributaría'),('ENF', 'Enfermería'),
		('INF', 'Informáica'),('MER', 'Mercadeo'),('TUR', 'Turismo'))
	Are_Alu = models.CharField('Area',max_length=3, choices=Are_Sel)
	Doc_Sel = (('AC', 'Acta De Nacimiento'),('CM', 'Certificado Médico'),('F2', 'Fotos 2x2'),('CG', 'Certificado de Grado'))
	Doc_Alu = MultiSelectField('Documentos',choices = Doc_Sel)
	Fot_Alu = models.CharField(max_length=6,blank=True,null=True)
	Tutore = models.ForeignKey(Tutore,null=True,blank=True,on_delete=models.CASCADE,verbose_name='Tutor')
	
	def _get_edad(self):
		return '%s' % (date.today().year - self.Fna_Alu.year)
	Edad = property(_get_edad)

	def InfAlumno(self):
		cAl = "{0},{1}"
		return cAl.format (self.Nom_Alu,self.Ape_Alu)
	def __str__(self):
		return self.InfAlumno()

#        edad = hoy.year - fechanacimiento.year - ((hoy.month, hoy.day) < (fechanacimiento.month, fechanacimiento.day))
       
class Empleado(models.Model):
	Id_Emp = models.AutoField('Identificación',primary_key=True)
	Nom_Emp = models.CharField('Nombre',max_length=30,blank=False,null=False)
	Dir_Emp = models.CharField('Dirección',max_length=40,blank=False,null=False)
	Nac_Emp = models.CharField('Nacionalidad',max_length=3,blank=True,null=True)
	Sex_SelE = (('F', 'Femenino'),('M', 'Masculino'))
	Sex_Emp = models.CharField('Sexo',max_length = 1, choices = Sex_SelE)
	Dpt_SelE = (('IDI', 'Idiomas'),('MAT', 'Matemáticas'),('SOC', 'Sociales'),
		('NAT', 'Naturales'),('TUR', 'Turismo'),('HUM', 'Humanidades'),
		('GES', 'Gestión Adm.'),('INF', 'Informatíca'),('ENF', 'Enfermería'),
		('CON', 'Contabilidad'),('MER', 'Mercadeo'),('AMD','Administrativo'))
	Dpt_Emp = models.CharField('Departamento',max_length=3, choices=Dpt_SelE)
	Cor_Emp = models.EmailField('Correo Electrónico',max_length=35,blank=True,null=True)	
	Fna_Emp = models.DateField('Fecha de Nacimiento')
	Tfi_Emp = models.CharField('Teléfono Fijo',max_length=15,blank=True,null=True)
	Tmo_Emp = models.CharField('Teléfono Móvil',max_length=15,blank=True,null=True)
	Tip_SelE = (('P', 'Profesor'),('M', 'Maestría'),('D', 'Doctorado'),('E', 'Empleado'))
	Tip_Emp = models.CharField('Titulación',max_length=1, choices=Tip_SelE)
	Tsa_Emp = models.CharField('Tipo de Sangre',max_length=10,blank=True,null=True)
	Car_SelC = (('A', 'Diector'),('B', 'Sub-Director Académico'),('C', 'Sub-Director Adm.'),
		('D', 'Maestro'),('E', 'Psicologo'),('F', 'Vinculacion Externa'),
		('G', 'Coordinacion Academica.'),('H', 'Coordinacion Tecnica'),('I', 'Contador'),
		('J', 'Apoyo'),('K', 'Conserje'),('L','Chofer'))
	Car_Emp = models.CharField('Cargo',max_length=1, choices=Car_SelC)
	Fot_Emp = models.ImageField(upload_to='D:\Colegio\FotEmp\FRANCIA.JPG')

	def InfEmpleado(self):
		cEm = "{0}"
		return cEm.format (self.Nom_Emp)

	def __str__(self):
		return self.InfEmpleado()

class Asignatura(models.Model):
	Id_Asi = models.CharField('Identificación',max_length=7,primary_key=True)
	Nom_Asi = models.CharField('Nombre',max_length=30,blank=False,null=False)
	Cho_Asi = models.IntegerField('Cantidad de Horas')
	Dpt_SelE = (('IDI', 'Idiomas'),('MAT', 'Matemáticas'),('SOC', 'Sociales'),
		('NAT', 'Naturales'),('TUR', 'Turismo'),('HUM', 'Humanidades'),
		('GES', 'Gestión'),('INF', 'Informática'),('ENF', 'Enfermería'),
		('CON', 'Contabilidad'),('MER', 'Mercadeo'),('ESP', 'Español'))
	Dpt_Asi = models.CharField('Departamento',max_length=3, choices=Dpt_SelE)
	Tip_Sela = (('A', 'Académica'),('T', 'Técnica'))
	Tip_Asi = models.CharField('Tipo Asignatura',max_length = 1, choices = Tip_Sela)
	def InfAsignatura(self):
		cAs = "{0} ,{1} ,{2}"
		return cAs.format (self.Id_Asi,self.Nom_Asi,self.Dpt_Asi)
	def __str__(self):
		return self.InfAsignatura()

class Grado(models.Model):
	Id_Gra = models.CharField('Id-Grado',max_length=7,primary_key=True)
	Empleado = models.ForeignKey(Empleado,null=True,blank=True,on_delete=models.CASCADE,verbose_name='Prof. Titular')
	Asi01 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi02 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi03 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi04 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi05 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi06 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi07 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi08 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi09 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi10 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi11 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi12 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi13 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi14 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi15 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	Asi16 = models.CharField('Asignatura',max_length=11,blank=True,null=True)
	def InfGrado(self):
		cGr = "{0} ,{1}"
		return cGr.format (self.Id_Gra,self.Empleado)
	def __str__(self):
		return self.InfGrado()


	
	
		