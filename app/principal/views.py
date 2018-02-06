from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from collections import OrderedDict
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect	
import json
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

from django.core import serializers
from app.principal.forms import *
from app.principal.models import *

from django.http import HttpResponse
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from io import BytesIO
from reportlab.lib.enums import TA_LEFT, TA_CENTER


# Create your views here.
def principal(request):
	
	productos=Producto.objects.all()

	if request.method == 'POST':
		form = ProductosHome(request.POST)
		form2 = Registros(request.POST)


		if form2.is_valid():
			form2.save()
	#	return HttpResponseRedirect('/principal/nuevo')
	else:

		form = ProductosHome()
		form2 = Registros()
	return render(request, 'principal/principal.html', {'form':form,'form2':form2,'productos':productos})

def principal_elemento(request):
	codigo = request.POST['codigo']
	concepto = request.POST['concepto']
	fecha = request.POST['fecha']
	entrada = request.POST['entrada']
	salida = request.POST['salida']
	saldo = request.POST['saldo']


	if request.method == 'POST':
		
		Registro.objects.create(codigo_id=codigo,concepto=concepto,fecha=fecha,entrada=entrada,salida=salida,saldo=saldo)

###########################################################################################################
################################     PRODUCTO       #######################################################
###########################################################################################################

def producto_nuevo(request):
	
	if request.method == 'POST':
		form = Productos(request.POST)
		if form.is_valid():
			form.save()
			
		return HttpResponseRedirect('/principal/nuevo')
	else:

		form = Productos()
		
	return render(request, 'principal/producto.html', {'form':form})

class producto_list(ListView):
	model = Producto
	template_name = 'principal/producto_listar.html'
	paginate_by = 10

def producto_listado(request):
	lista= serializers.serialize('json',Producto.objects.all(), fields=['codigo','nombre'])
	return HttpResponse(lista,content_type='application/json')
###########################################################################################################
################################     Registro       #######################################################
###########################################################################################################

def registro_nuevo(request):
	
	productos=Producto.objects.all()


	form = Registro()
	form2 = ProductosHome()
		
	return render(request, 'principal/registro_imprimir.html', {'form':form,'form2':form2,'productos':productos})



###########################################################################################################
################################     AJAX       ###########################################################
###########################################################################################################

class busquedaNombre(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		nombre = Producto.objects.filter(codigo=cod)
		
		data = serializers.serialize('json', nombre, fields=('nombre'))

		return HttpResponse(data, content_type='application/json')

class busquedaElementos(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		elementos = Registro.objects.filter(codigo=cod).order_by('fecha')
		
		data = serializers.serialize('json', elementos, fields=('codigo','fecha','concepto','entrada','salida','saldo'))

		return HttpResponse(data, content_type='application/json')

class busquedaFechas(TemplateView):
	def get(self,request,*args,**kwargs):
		cod = request.GET['codigo']
		fechas = Registro.objects.filter(codigo=cod).order_by('fecha')
		
		data = serializers.serialize('json', fechas, fields=('fecha'))

		return HttpResponse(data, content_type='application/json')

###########################################################################################################
################################     IMPRESION       ######################################################
###########################################################################################################

def generar_pdf(request,codigo,fecha1,fecha2):
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "producto.pdf"  # llamado producto
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=20,
                            leftMargin=20,
                            topMargin=60,
                            bottomMargin=18,
                            )
    doc.title = codigo+"_"+fecha1+"-"+fecha2
    clientes = []
    styles = getSampleStyleSheet()
    headerStyle = ParagraphStyle(
            name='Total',
            fontSize=18,
            fontName='Helvetica-BoldOblique',
            textColor=colors.black,
            spaceBefore=0.5 * cm,
            spaceAfter=0.5 * cm,
            alignment=TA_CENTER)
    parrafoStyle = ParagraphStyle(
            name='Total1',
            fontSize=12,
            fontName='Helvetica',
            textColor=colors.black,
            spaceBefore=0.5 * cm,
            spaceAfter=0.5 * cm,
            alignment=TA_CENTER)

    nombre = Producto.objects.get(codigo=codigo)
    text= "Registros de "+nombre.nombre
    p1 = Paragraph(text, headerStyle)
    text= "\n"
    salto = Paragraph(text, headerStyle)
    text = "Codigo del Producto "+codigo
    p2= Paragraph(text,parrafoStyle)
    text = "Del "+fecha1+" al "+fecha2
    p3 = Paragraph(text,parrafoStyle)
    #header = Paragraph("Listado de Productos", styles['ps'])
    clientes.append(p1)
    clientes.append(salto)
    clientes.append(p2)
    clientes.append(p3)
    headings = ('Fecha', 'Concepto', 'Entradas', 'Salidas', 'Saldo')
    allclientes = [(p.fecha, p.concepto, p.entrada, p.salida, p.saldo) for p in Registro.objects.filter(codigo=codigo,fecha__range=(fecha1,fecha2)).order_by('fecha')]

    t = Table([headings] + allclientes)
    t.setStyle(TableStyle( 
        [
            ('GRID', (0, 0), (4, -1), 1, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ],
    ))
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response

