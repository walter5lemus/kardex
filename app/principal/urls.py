from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.principal.views import *

urlpatterns = [
 url(r'^nuevo', principal1, name= 'principal'),

]