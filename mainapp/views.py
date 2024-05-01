from django.shortcuts import render
from mainapp.models import ImageOfTheDay
import requests
from django.utils import timezone
from datetime import datetime
import json
import webbrowser
import pytz


def index(request):
    FechaActualizada = comprobarFechaAPOD(request)

    if not FechaActualizada:
        print("FECHA DESACTUALIZADA, CREANDO NUEVO REGISTRO")
        nasaAPOD(request)
    else:
        print("no fue necesario actualizar registro")

    ultimoRegistro = ImageOfTheDay.objects.latest("last_updated")
    imagen_del_diaURL = ultimoRegistro.image_url
    print(f"{imagen_del_diaURL} url a mandar a index")

    return render(request, 'mainapp/index.html', {
        'title': 'inicio',
        'imageOfTheDay' : imagen_del_diaURL
    })


def about(request):
    return render(request, 'mainapp/about.html', {  
        'title': 'sobre nosotros'
    })

def contacto(request):
    return render(request, 'mainapp/contacto.html')


def experiencia(request):
    return render(request, 'mainapp/experiencia.html')

def comprobarFechaAPOD(request):
    zona_horaria = pytz.timezone('America/Mexico_City')
    fecha_hora_actual = datetime.now(zona_horaria)
    fecha_actual = fecha_hora_actual.date()



    ultimo_registro = ImageOfTheDay.objects.latest("last_updated")
    fecha_ultimo_registro = ultimo_registro.last_updated
    print(f"el ultimo registro fue realizado el: {fecha_ultimo_registro}" )
    print(f" fecha actual: {fecha_actual}")

    if fecha_actual == fecha_ultimo_registro:
        return True
    else :
        return False

def nasaAPOD(request):
    zona_horaria = pytz.timezone('America/Mexico_City')
    fecha_hora_actual = datetime.now(zona_horaria)
    fecha_actual = fecha_hora_actual.date()

    print(f"la fecha de hoy es {fecha_actual}")
    API_KEY = 'zMm2wEorcFjh2W3pbUnPMQwEbMb1PYxD6CdQTKpu'
    url = 'https://api.nasa.gov/planetary/apod'
    print("url enviado")
    params = {
        'api_key': API_KEY,
        'hd': 'False',
        'date': fecha_actual
    }


    response = requests.get(url, params=params)
    json_data = json.loads(response.text)
    print(json_data)
    image_url = json_data['url']

    # Crear una nueva instancia de ImageOfTheDay y guardarla en la base de datos
    nueva_imagen = ImageOfTheDay.objects.create(image_url=image_url, last_updated=datetime.now().date())

    return nueva_imagen

    
# Create your views here.