# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from app.principal.models import *
from django.contrib.admin import widgets
#from app.informacion.choices import *

class Productos(forms.ModelForm):
	class Meta:
		model = Producto

		fields = [
			'codigo',
			'nombre',
		]

		labels={
			'codigo': 'Codigo Producto'	,
			'nombre': 'Nombre'	,
		}

		widgets={
			'codigo': forms.TextInput(attrs={'class':'form-control','required': True,'pattern':'[0-9]{8}','title':'Codigo Mal Escrito!!! Por Favor dijite el codigo como el siguiente\nEjemplo: 00000001'}),
			'nombre': forms.TextInput(attrs={'class':'form-control','required': True}),
			
		}

class ProductosHome(forms.ModelForm):
	class Meta:
		model = Producto

		fields = [
			'codigo',
			'nombre',
		]

		labels={
			'codigo': 'Codigo Producto'	,
			'nombre': 'Nombre'	,
		}

		widgets={
			'codigo': forms.Select(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			
		}

class Registros(forms.ModelForm):
	class Meta:
		model = Registro

		fields = [
			'codigo',
			'fecha',
			'concepto',
			'entrada',
			'salida',
			'saldo',
		]

		labels={

			'codigo': 'Codigo Produto'	,
			'fecha': 'Fecha',
			'concepto': 'Concepto',
			'entrada': 'Entradas',
			'salida':'Salidas',
			'saldo':'Saldo',
		}

		widgets={
			'codigo': forms.HiddenInput(attrs={'class':'form-control','id':'id_codigo2'}),
			'fecha': forms.TextInput(attrs={'class':'form-control'}),
			'concepto': forms.Textarea(attrs={'class':'form-control','rows':5, 'cols':3}),	
			'entrada': forms.NumberInput(attrs={'class':'form-control','min':1}),
			'salida':forms.NumberInput(attrs={'class':'form-control','min':1}),
			'saldo':forms.NumberInput(attrs={'class':'form-control','min':0,'readonly':True}),
			
		}
		