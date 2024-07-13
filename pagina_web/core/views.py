from django.shortcuts import render
from .models import *
import requests
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    	return render(request, 'core/index.html')

def Autores(request):
    biografia = Autor.objects.all()
    paginator = Paginator(biografia, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'core/autor.html', context)

def Libros(request):
    biblio = Libro.objects.all()
    paginator = Paginator(biblio, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
    }

    return render(request, 'core/libro.html',context)

