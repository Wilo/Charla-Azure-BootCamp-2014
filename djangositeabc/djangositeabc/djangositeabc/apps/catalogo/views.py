# -*- coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from .models import *
from django.http import HttpResponse

def index(request):
    return render_to_response('catalogo/index.html', context_instance=RequestContext(request))
def header(request):
    return render_to_response('catalogo/header.html', context_instance=RequestContext(request))

def CiudadelaView(request):
    return render_to_response('catalogo/ciudadela.html', context_instance=RequestContext(request))

def serializaCiudadela(request):
    data = Ciudadela.objects.all()
    resultado = []
    for Datos in data:
        serializado = {}
        serializado ['id'] = str(Datos.pk)
        serializado ['Descripcion'] = Datos.Descripcion
        resultado.append(serializado)
    Json = json.dumps(resultado)
    return HttpResponse(Json, mimetype="application/json")

@csrf_exempt
def InsertCiudadela(request):
    if request.method == 'POST':
        descripcion = request.POST['Descripcion']
        print descripcion
        ciu = Ciudadela(Descripcion=descripcion, Fecha=datetime.today())
        print ciu
        ciu.save()
        return HttpResponse('Success', mimetype="application/json")
    else:
        return HttpResponse('Error')

@csrf_exempt
def UpdateCiudadela(request, id):
    if request.method == "POST":
        id = id
        desc = request.POST['Descripcion']
        ciudadela = Ciudadela.objects.get(id=id)
        ciudadela.Descripcion = desc
        ciudadela.Fecha = datetime.today()
        ciudadela.save()
        return HttpResponse('Success')
    else:
        return HttpResponse('Fail')

@csrf_exempt
def EliminaCiudadela(request,id):
    if request.POST:
        id = id
        ciudadela = Ciudadela.objects.get(id= id)
        print ciudadela
        ciudadela.delete()
        return HttpResponse('Success')
    else:
        return HttpResponse('Fail')

def contact(request):
    return render_to_response('catalogo/contactar.html', context_instance=RequestContext(request))

def xml_render(request):
    xml = serializers.serialize('xml',Ciudadela.objects.all(),fields=("id","Descripcion",) )
    return HttpResponse(xml,mimetype="application/xml")

def yaml_render(request):
    yaml = serializers.serialize('yaml',Ciudadela.objects.all(),fields=("id","Descripcion",) )
    return HttpResponse(yaml)