# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin import widgets
from app.analisis_cefalometrico.models import *

class analisis_cefalometricoForm(forms.ModelForm):
	class Meta:
		model = analisis_cefalometrico

		fields = [	
			'fichas',
		]

		labels = {
			'fichas': 'Numero de ficha',
		}

		widgets = {
			'fichas': forms.HiddenInput(attrs={'class':'form-control'}),
		}
