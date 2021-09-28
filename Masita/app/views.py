from django.shortcuts import render

from .models import Pasteleria, Desayuno

def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def blog(request):
    todos_los_proyectos =  Pasteleria.objects.all()
    proyectos =  Desayuno.objects.all()
    return render(request, 'app/blog.html', {'pasteleria': todos_los_proyectos,'desayuno': proyectos})

def contact(request):
    return render(request, 'app/contact.html')

def recipe(request):
    return render(request, 'app/recipe.html')