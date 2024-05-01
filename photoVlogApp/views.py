from django.shortcuts import render,  HttpResponse
from photoVlogApp.models import Publicacion

def publicacionDetalle(request, id):
    publicacion = Publicacion.objects.get(pk =id)
    return HttpResponse(publicacion.titulo, publicacion.descripcion)

def publicaciones(request): 
    publicaciones = Publicacion.objects.order_by('id')
    print(f"publicaciones todas: {publicaciones}")
    return render(request , 'imagenes.html', {
            'publicaciones': publicaciones
         })

def CategoriaImgs(request):
    return render(request, 'categorias.html')

def LugaresImgs(request):
    return render(request,'lugares.html')

def ColoresImgs(request):
    return render(request, 'colores.html')

def returnThumbnails(request):
    thumbs = Publicacion.objects.filter(esThumbLugares=True)
    print(f"se llama thumbs {thumbs}")  
    return render(request, 'lugares.html', {'thumbs': thumbs})  

def returnLugares(request, lugar):
    Lugar = Publicacion.objects.filter(lugar = lugar)
    print(f"solicitando lugares de publicacion {Lugar}")
    return render(request, 'lugar.html', {'Lugar' : Lugar})

def returnThumbCategorias(request):
    thumbscategorias = Publicacion.objects.filter(esThumbCategorias = True)
    print(f" categorias traidas {thumbscategorias}")
    return render(request,'categorias.html', {'thumbscategorias':thumbscategorias})

def returnCategoria(request, categoria):
    categoria = Publicacion.objects.filter(categoria = categoria)
    print(f"categorias traidas: {categoria}")
    return render(request, 'categoria.html', {"Categoria" : categoria})

"""para hacer la galeria mas facil puedo usar esta libreria de tailwind https://flowbite.com/docs/components/gallery/"""