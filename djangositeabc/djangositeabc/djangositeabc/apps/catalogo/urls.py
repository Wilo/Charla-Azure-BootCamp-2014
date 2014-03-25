#!/usr/bin/env python
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('djangositeabc.apps.catalogo.views',
                          url(r'^$','index',name='vista_principal'),
                          url(r'^index/header$','header', name='header'),
                          url(r'^ciudadela/$','CiudadelaView'),
                          url(r'^ciudadela/read/$', 'serializaCiudadela', name="ConsumeCiudadela"),
                          url(r'^ciudadela/read/xml/$', 'xml_render', name="ciudadelaXML"),
                          url(r'^ciudadela/read/yaml/$', 'yaml_render', name="ciudadelaYAML"),
                          url(r'^ciudadela/add/$','InsertCiudadela',name='RegistraCiudadela'),
                          url(r'^ciudadela/edit/(\d+)$','UpdateCiudadela'),
                          url(r'^ciudadela/del/(\d+)$','EliminaCiudadela'),
                          url(r'^contact/$','contact'),  
)