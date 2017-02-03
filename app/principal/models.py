from __future__ import unicode_literals	
from django.db import models

# Create your models here.

class Producto(models.Model):
	codigo = models.CharField(max_length=50,primary_key=True)
	nombre = models.CharField(max_length=70)


	def __unicode__(self):
		return  '{}'.format(self.codigo)

class Registro(models.Model):
	codigo =models.ForeignKey(Producto,null=False, blank=False, on_delete=models.CASCADE)
	fecha = models.DateField()
	concepto = models.CharField(max_length=200)
	entrada = models.IntegerField(null=True, blank=True)
	salida = models.IntegerField(null=True, blank=True)
	saldo = models.IntegerField()

	def __unicode__(self):
		return  '{}'.format(self.codigo)

