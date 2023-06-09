from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Book, BookReview


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        exclude = ['slug']


class ReviewForm(forms.ModelForm):

    class Meta:
        model = BookReview
        exclude = ['user', 'book']

    def __init__(self, user, book, *args, **kwargs):
        self.user = user
        self.book = book
        super(ReviewForm, self).__init__(*args, **kwargs)


class BookSearchForm(forms.Form):
    title = forms.CharField(required=False)


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]
