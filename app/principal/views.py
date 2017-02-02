from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from collections import OrderedDict
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect	
import json
from django.core import serializers
from app.principal.forms import *
from app.principal.models import *

# Create your views here.
def principal(request):
	
	productos=Producto.objects.all()

	if request.method == 'POST':
		form = ProductosHome(request.POST)
		form = Registros(request.POST)


		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
		return HttpResponseRedirect('/')
	else:

		form = ProductosHome()
		form2 = Registros()
	return render(request, 'principal/principal.html', {'form':form,'form2':form2,'productos':productos})

def producto_nuevo(request):
	
	if request.method == 'POST':
		form = Productos(request.POST)
		if form.is_valid():
			form.save()
			
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	else:

		form = Productos()
		
	return render(request, 'principal/producto.html', {'form':form})

def registro_nuevo(request):
	if request.method == 'POST':
		form = Registros(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('<script type="text/javascript">window.close()</script>')

	else:

		form = Registros()
		
	return render(request, 'principal/registro.html', {'form':form})




class busquedaNombre(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		nombre = Producto.objects.filter(codigo=cod)
		
		data = serializers.serialize('json', nombre, fields=('nombre'))

		return HttpResponse(data, content_type='application/json')