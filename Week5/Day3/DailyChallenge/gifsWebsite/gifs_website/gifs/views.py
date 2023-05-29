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
    current_gif = Gif.objects.get(id=pk)

    if request.method == "POST":
        if 'like' in request.POST:
            current_gif.likes += 1
            current_gif.save()
        elif 'dislike' in request.POST:
            current_gif.likes -= 1
            current_gif.save()

    context = {
        'gif': current_gif,
    }
    return render(request, 'gifs/gif.html', context)


def liked_gifs(request):
    gifs = Gif.objects.all()
    context = dict()
    gifs = [g for g in gifs if g.likes > 0]
    context['gifs'] = sorted(gifs, key=lambda x: x.likes, reverse=True)

    return render(request, 'gifs/liked_gifs.html', context)


def categories(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'gifs/categories.html', context)
