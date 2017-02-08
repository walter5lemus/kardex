from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.principal.views import *

urlpatterns = [
	url(r'^$', login_required(principal), name= 'principal'),
	url(r'^nuevo/', login_required(principal), name= 'principal'),
	url(r'^nuevo/elemento/', login_required(principal_elemento), name= 'principal_elemento'),

	url(r'^producto/$',login_required(producto_nuevo), name= 'nuevo_producto'),
	url(r'^producto/listar/',login_required(producto_list.as_view()), name= 'producto_listar'),

	url(r'^registro/$',login_required(registro_nuevo), name= 'registro_nuevo'),


	url(r'^buscar/nombre/',login_required(busquedaNombre.as_view()),name='busqueda_nombre'),
	url(r'^buscar/elementos/',login_required(busquedaElementos.as_view()),name='busqueda_elemento'),
	url(r'^buscar/fechas/',login_required(busquedaFechas.as_view()),name='busqueda_fechas'),

	url(r'^reporte/(?P<codigo>[0-9]{8})/(?P<fecha1>\d{4}[-/]\d{2}[-/]\d{2})/(?P<fecha2>\d{4}[-/]\d{2}[-/]\d{2})/',login_required(generar_pdf),name='reporte'),

]
