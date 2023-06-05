from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from .models import Film, Director
from .forms import FilmForm, DirectorForm, ReviewForm
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from accounts.models import CustomUser


class HomePageView(generic.ListView):
    template_name = 'homepage.html'
    context_object_name = 'films'
    queryset = Film.objects.order_by('release_date')
    model = Film

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['title'] = "IMDI | Homepage"
        return context


class FilmCreateView(UserPassesTestMixin, generic.CreateView):
    template_name = 'film/add_film.html'
    form_class = FilmForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context = super(FilmCreateView, self).get_context_data(**kwargs)
        context['title'] = "Add Film"
        return context

    def test_func(self):
        return self.request.user.is_superuser


class DirectorCreateView(UserPassesTestMixin, generic.CreateView):
    template_name = 'director/add_director.html'
    form_class = DirectorForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context = super(DirectorCreateView, self).get_context_data(**kwargs)
        context['title'] = "Add Director"
        return context

    def test_func(self):
        return self.request.user.is_superuser


class ReviewCreateView(generic.CreateView):
    template_name = 'review/add_review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        context['title'] = "Add Review"
        return context


class FilmUpdateView(UserPassesTestMixin, generic.edit.UpdateView):
    template_name = 'film/add_film.html'
    model = Film

    fields = '__all__'

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context = super(FilmUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Update Film"
        return context

    def test_func(self):
        return self.request.user.is_superuser


class DirectorUpdateView(UserPassesTestMixin, generic.edit.UpdateView):
    template_name = 'director/add_director.html'
    model = Director

    fields = '__all__'

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context = super(DirectorUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Update Director"
        return context

    def test_func(self):
        return self.request.user.is_superuser


class FilmDeleteView(UserPassesTestMixin, generic.edit.DeleteView):
    template_name = 'film/confirm_delete.html'
    model = Film
    success_message = "The film was deleted successfully."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(FilmDeleteView, self).form_valid(form)

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context = super(FilmDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Confirm film deletion"
        return context

    def test_func(self):
        return self.request.user.is_superuser


class FavoriteFilmView(generic.View):
    model = CustomUser

    def post(self, request, pk):
        user = request.user
        film = Film.objects.get(id=pk)

        if film in user.favorite_films.all():
            user.favorite_films.remove(film)
        else:
            user.favorite_films.add(film)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class FilmDetailView(generic.DetailView):
    model = Film
    template_name = 'film/film_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FilmDetailView, self).get_context_data(**kwargs)
        context['title'] = Film.objects.get(id=self.kwargs["pk"]).title
        return context

    def get_queryset(self, **kwargs):
        return Film.objects.filter(id=self.kwargs["pk"])
