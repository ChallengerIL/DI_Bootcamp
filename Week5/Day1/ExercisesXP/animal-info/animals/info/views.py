from django.shortcuts import render
from os.path import dirname, join
import json

CURRENT_DIR = dirname(__file__)
JSON_FILE = "./../animals.json"
FILE_PATH = join(CURRENT_DIR, JSON_FILE)

with open(FILE_PATH) as f:
    data = json.load(f)
    context = {
        'animals': data['animals'],
        'families': data['families'],
    }


def animal(request, pk):
    context['pk'] = pk
    return render(request, 'info/animals.html', context)


def family(request, pk):
    context['pk'] = pk
    return render(request, 'info/families.html', context)
