from django.shortcuts import render, redirect
from .models import Film
from .forms import AddFilmForm, AddDirectorForm


def homepage(request):
    context = {
        'page_title': "IMDI | Homepage",
        'films': Film.objects.order_by('release_date'),
    }
    return render(request, 'homepage.html', context)


def add_film(request):
    if request.method == "POST":
        form = AddFilmForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("homepage")
    else:
        form = AddFilmForm()

    context = {
        'page_title': "Add Film",
        'form': form,
    }
    return render(request, 'film/add_film.html', context)


def add_director(request):
    if request.method == "POST":
        form = AddDirectorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("homepage")
    else:
        form = AddDirectorForm()

    context = {
        'page_title': "Add Director",
        'form': form,
    }
    return render(request, 'director/add_director.html', context)
