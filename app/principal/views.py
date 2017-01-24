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
def principal1(request):
	
	if request.method == 'POST':
		form = Productos(request.POST,initial={})
		form2 = Registros(request.POST,initial={})
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
		return HttpResponseRedirect('/')
	else:

		form = Productos(initial={})
		form2 = Registros(initial={})
	return render(request, 'principal/principal2.html', {'form':form,'form2':form2})
