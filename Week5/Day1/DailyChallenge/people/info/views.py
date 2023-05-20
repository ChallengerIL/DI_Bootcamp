from django.shortcuts import render
from os.path import dirname, join

people_list = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

context = {
    'people': people_list,
}


def people(request):
    new_context = dict()
    new_context['people'] = sorted(context['people'], key=lambda x:x['age'])
    return render(request, 'info/people.html', new_context)


def person(request, pk):
    context['pk'] = pk
    return render(request, 'info/person.html', context)
