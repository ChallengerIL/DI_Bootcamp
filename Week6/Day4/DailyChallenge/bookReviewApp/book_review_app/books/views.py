from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Avg
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Book
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm, ProfileForm, BookForm, BookSearchForm, ReviewForm


class HomePageView(generic.ListView):
    template_name = 'books/homepage.html'
    context_object_name = 'books'
    queryset = Book.objects.all()
    model = Book

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['page_title'] = "Book Review App | Homepage"
        return context


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class LoginPageView(generic.View):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('homepage')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


def logout_view(request):
    logout(request)


class ProfileView(generic.UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('homepage')
    template_name = 'registration/profile.html'


class BookCreateView(UserPassesTestMixin, generic.CreateView):
    template_name = 'books/add_book.html'
    form_class = BookForm

    def form_valid(self, form):
        book = form.save(commit=False)
        book.user = self.request.user
        book.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super(BookCreateView, self).get_context_data(**kwargs)
        context['title'] = "Add Book"
        return context

    def test_func(self):
        return self.request.user.is_authenticated


class BookSearchView(generic.ListView):
    template_name = 'books/search.html'
    context_object_name = 'books'
    form_class = BookSearchForm
    model = Book
    queryset = model.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')

        if query:
            return qs.filter(title__icontains=query)
        return None


class BookDetailView(FormMixin, generic.DetailView):
    template_name = 'books/book.html'
    model = Book
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        book = Book.objects.get(slug=self.kwargs['slug'])
        reviews = book.reviews.all()

        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['book'] = book
        context['title'] = book.title
        context['reviews'] = reviews
        context['avg_rating'] = reviews.aggregate(Avg('rating'))['rating__avg']
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        kwargs["book"] = Book.objects.get(slug=self.kwargs['slug'])
        return kwargs

    def get_success_url(self):
        return reverse('book', kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        review_instance = form.save(commit=False)
        review_instance.user = self.request.user
        review_instance.book = Book.objects.get(slug=self.kwargs['slug'])
        review_instance.save()

        return super(BookDetailView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('homepage')

        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

