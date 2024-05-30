from properties.models import Property
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm

def first_view(request):
    if request.user.is_authenticated:
        properties = Property.objects.exclude(owner=request.user)
    else:
        properties = Property.objects.all()
    context = {
        "properties": properties
    }
    return render(request, "base.html", context=context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registro.html', { 'form': form})
    

    
#SCRAPING
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def scraping_view(request):
    # Realizar la solicitud a la página web
    url = 'https://listado.mercadolibre.com.mx/terrenos-tuxtla-gutierrez#D[A:terrenos%20tuxtla%20gutierrez]'
    page = requests.get(url)
    
    # Parsear el contenido de la página
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Obtener elementos utilizando BeautifulSoup
    terrenos = []
    for item in soup.find_all('li', class_='ui-search-layout__item'):
        title_elem = item.find('h2', class_='ui-search-item__title')
        title = title_elem.text.strip() if title_elem else 'No title'
        
        terrenos.append(title)
    
    # Imprimir los datos obtenidos (para depuración)
    print(terrenos)
    
    # Renderizar la respuesta
    return render(request, 'scraped_data.html', {'terrenos': terrenos})

