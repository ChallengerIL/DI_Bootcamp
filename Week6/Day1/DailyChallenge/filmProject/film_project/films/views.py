from django.shortcuts import reverse
from .models import Film
from .forms import FilmForm, DirectorForm, ReviewForm
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
    form_class = FilmForm

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
    form_class = DirectorForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context = super(DirectorCreateView, self).get_context_data(**kwargs)
        context['page_title'] = "Add Director"
        return context


class ReviewCreateView(generic.CreateView):
    template_name = 'review/add_review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('homepage')

    def get_context_data(self, **kwargs):
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        context['page_title'] = "Add Review"
        return context
