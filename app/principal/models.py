from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return '{} {}'.format(self.codigo, self.nombre)

class Kardex(models.Model):
	entrada = models.ForeignKey(Codigo, null=False, blank=False, on_delete=models.CASCADE)
	fecha = models.DateField()
	concepto = models.CharField(max_length=100)
	entrada = models.IntegerField()
	precio_entrada = models.FloatField(null=True, blank=True)
	salida = models.IntegerField()
	precio_salida = models.FloatField(null=True,blank=True)
	saldo = models.FloatField()

	def __unicode__(self):
        return '{}'.format(self.codigo)


