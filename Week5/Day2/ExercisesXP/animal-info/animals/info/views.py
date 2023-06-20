from django.shortcuts import render
from .models import Family, Animal


def animals(request):
    context = {
        'page_title': "A list of animals",
        'animals': Animal.objects.all(),
    }
    return render(request, 'info/animals.html', context)


def animal(request, pk):
    context = {
        'animal': Animal.objects.get(id=pk),
    }
    return render(request, 'info/animal.html', context)


def family(request, pk):
    context = {
        'family': Family.objects.get(id=pk),
        'animals': Animal.objects.filter(family=pk),
    }
    return render(request, 'info/family.html', context)
