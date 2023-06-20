from django.shortcuts import render, redirect
from .models import Gif, Category
from .forms import GifForm, CategoryForm


def homepage(request):
    context = {
        'page_title': "Gifs | Homepage",
        'gifs': Gif.objects.all(),
    }
    return render(request, 'gifs/homepage.html', context)


def add_new_gif(request):
    if request.method == "POST":
        form = GifForm(request.POST)

        if form.is_valid():
            chosen_categories = form.cleaned_data.get('categories')
            gif_instance = form.save()

            for cat in chosen_categories:
                cat.gifs.add(gif_instance)

            return redirect("homepage")
    else:
        form = GifForm()

    return render(request, "gifs/add_new_gif.html", {"form": form})


def add_new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = CategoryForm()

    return render(request, "gifs/add_new_category.html", {"form": form})


def category(request, pk):
    context = {
        'category': Category.objects.get(id=pk),
    }
    return render(request, 'gifs/category.html', context)


def gif(request, pk):
    context = {
        'gif': Gif.objects.get(id=pk),
    }
    return render(request, 'gifs/gif.html', context)


def categories(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'gifs/categories.html', context)
