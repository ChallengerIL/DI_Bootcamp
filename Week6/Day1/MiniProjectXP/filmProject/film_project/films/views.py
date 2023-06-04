from django.shortcuts import render, redirect, reverse
from .models import Film
from .forms import AddFilmForm, AddDirectorForm
from django.views import generic


class HomePageView(generic.ListView):
    template_name = 'homepage.html'
    context_object_name = 'films'
    queryset = Film.objects.order_by('release_date')
    model = Film

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['page_title'] = "IMDI | Homepage"
        return context


class FilmCreateView(generic.CreateView):
    template_name = 'film/add_film.html'
    form_class = AddFilmForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context = super(FilmCreateView, self).get_context_data(**kwargs)
        context['page_title'] = "Add Film"
        return context


class DirectorCreateView(generic.CreateView):
    template_name = 'director/add_director.html'
    form_class = AddDirectorForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context = super(DirectorCreateView, self).get_context_data(**kwargs)
        context['page_title'] = "Add Director"
        return context


# def homepage(request):
#     context = {
#         'page_title': "IMDI | Homepage",
#         'films': Film.objects.order_by('release_date'),
#     }
#     return render(request, 'homepage.html', context)


# def add_film(request):
#     if request.method == "POST":
#         form = AddFilmForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             return redirect("homepage")
#     else:
#         form = AddFilmForm()
#
#     context = {
#         'page_title': "Add Film",
#         'form': form,
#     }
#     return render(request, 'film/add_film.html', context)


# def add_director(request):
#     if request.method == "POST":
#         form = AddDirectorForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             return redirect("homepage")
#     else:
#         form = AddDirectorForm()
#
#     context = {
#         'page_title': "Add Director",
#         'form': form,
#     }
#     return render(request, 'director/add_director.html', context)
