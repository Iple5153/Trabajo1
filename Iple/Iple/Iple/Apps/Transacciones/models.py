from django.db import models
from Iple.Apps.Transacciones.models import *
from Iple.Apps.GestionAcademica.models import *

# Create your models here.
class Nota(models.Model):
	Lec_Not = models.CharField('Año Léctivo',max_length=9,blank=True,null=True)
	Asignatura = models.ForeignKey(Asignatura,null=True,blank=True,on_delete=models.CASCADE)
	Grado = models.ForeignKey(Grado,null=True,blank=True,on_delete=models.CASCADE)
	Alumno = models.ForeignKey(Alumno,null=True,blank=True,on_delete=models.CASCADE)
	Nt1_Not = models.IntegerField('Ago-Oct',blank=True,null=True)
	Nt2_Not = models.IntegerField('Nov-Ene',blank=True,null=True)
	Nt3_Not = models.IntegerField('Feb-Mar',blank=True,null=True)
	Nt4_Not = models.IntegerField('Abr-Jun',blank=True,null=True)
	Pfi_Not = models.IntegerField('P. Final',blank=True,null=True)
	Pco_Not = models.IntegerField('Completivo',blank=True,null=True)
	Pex_Not = models.IntegerField('Extraordinario',blank=True,null=True)
		
	def InfNota(self):
		cNO = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}"
		return cNO.format (self.Lec_Not,self.Asignatura,self.Grado,self.Alumno,self.Nt1_Not,self.Nt2_Not,self.Nt3_Not,self.Nt4_Not,self.Pfi_Not,self.Pco_Not,self.Pex_Not)

	def __str__(self):
		return self.InfNota()

class Cobro(models.Model):
	Nco_Cob = models.AutoField('No. Recibo',primary_key=True)
	Fco_Cob = models.DateField('Fecha Recibo')
	Mco_Cob = models.DecimalField('Monto del Recibo',max_digits=8,decimal_places=2)
	Con_Cob = models.CharField('Concepto',max_length=50,null=True,blank=True)
		
	def InfCobro(self):
		cCO = "{0},{1},{2},{3}"
		return cCO.format (self.Nco_Cob,self.Fco_Cob,self.Mco_Cob,self.Con_Cob)

	def __str__(self):
		return self.InfCobro()

class Psicologia(models.Model):
	Nre_Psi = models.AutoField('No. Recibo',primary_key=True)
	Tre_Sel = (('AU', 'Autorizacion'),('EX', 'Excusa'),('RE', 'Reporte'),('RT', 'Retiro'))
	Tre_Psi = models.CharField('Tipos De Reporte',max_length = 2, choices = Tre_Sel)
	Fre_Psi = models.DateField('Fecha Reporte',auto_now=False)
	Grado = models.ForeignKey(Grado,null=True,blank=True,on_delete=models.CASCADE)
	Alumno = models.ForeignKey(Alumno,null=True,blank=True,on_delete=models.CASCADE)
	Empleado = models.ForeignKey(Empleado,null=True,blank=True,on_delete=models.CASCADE,verbose_name='Profesor/Empleado')
	Mre_Psi = models.TextField('Motivo',null=True,blank=True)
	Rec_Psi = models.TextField('Recomendación',null=True,blank=True)
	def InfPsicologia(self):
		cPS = "{0},{1},{2},{3},{4},{5},{6},{7}"
		return cPS.format (self.Nre_Psi,self.Tre_Psi,self.Fre_Psi,self.Grado,self.Alumno,self.Empleado,self.Mre_Psi,self.Rec_Psi)

	def __str__(self):
		return self.InfPsicologia()
