from django.shortcuts import render
from .models import Registro
from django.shortcuts import render
import json
# Create your views here.


def home(request):
    return render(request, 'index.html')


def obtain_data(request):
    with open('application/Datos-ONIET---Hoja-1---JSON (1).json', 'r') as archivo:
        data = json.load(archivo)
        for item in data:
            duplicate = Registro.objects.filter(registro= item['Registro'])
            if duplicate:
                continue
            else:
                Registro.objects.create(registro=item['Registro'],empresa=item['Empresa'],mes=item['Mes'],produccionTotal=item['ProduccionTotal'],cantidaPiezasConFallas=item['CantidaPiezasConFallas'])

    registros = Registro.objects.all()
    empresas = []
    for registro in registros:
        nom_empresa = registro.empresa
        if nom_empresa not in empresas:
            empresas.append(nom_empresa)
    print(empresas)

    resultados_empresas = []

    for empresa in empresas:
        registros = Registro.objects.filter(empresa=empresa)
        produccion_total = 0
        cantidadPiezasConFallas = 0
        for registro in registros:
            produccion_total += registro.produccionTotal
            cantidadPiezasConFallas += registro.cantidaPiezasConFallas
        cantidadPiezasOk = produccion_total - cantidadPiezasConFallas

        empresa_dict = {
            "nombre": empresa,
            "produccionTotal": produccion_total,
            "cantidadPiezasOk": cantidadPiezasOk,
            "cantidadPiezasError": cantidadPiezasConFallas,
            "porcPiezasOk": round(cantidadPiezasOk / produccion_total, 2) ,
            "porcPiezasError": round(cantidadPiezasConFallas / produccion_total, 2)
        }
        resultados_empresas.append(empresa_dict)

    ordenados = sorted(resultados_empresas, key=lambda empresa:empresa['porcPiezasOk'], reverse=True)
    return render(request, 'index.html', context={'data': ordenados})