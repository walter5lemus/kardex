from django.db import models

# Create your models here.

class Producto(models.Model):
	codigo = models.CharField(max_length=50,primary_key=True)
	nombre = models.CharField(max_length=70)


	def __str__(self):
		return  '{} {}'.format(self.codigo, self.nombre)

class Registro(models.Model):
	codigo =models.ForeignKey(Producto,null=False, blank=False, on_delete=models.CASCADE)
	fecha = models.DateField()
	concepto = models.CharField(max_length=200)
	razones = models.TextField()
	entrada = models.IntegerField()
	salida = models.IntegerField()
	saldo = models.IntegerField()

	def __str__(self):
		return  '{} {}'.format(self.codigo, self.fecha)

