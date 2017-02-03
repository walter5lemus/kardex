from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.principal.views import *

urlpatterns = [
	url(r'^nuevo', principal, name= 'principal'),
	url(r'^producto',producto_nuevo, name= 'nuevo_producto'),
	url(r'^registro/(?P<codigo>[0-9]{8})',registro_nuevo, name= 'nuevo_registro'),

	url(r'^buscar/nombre/',busquedaNombre.as_view(),name='busqueda_nombre'),
	url(r'^buscar/elementos/',busquedaElementos.as_view(),name='busqueda_elemento'),

]
