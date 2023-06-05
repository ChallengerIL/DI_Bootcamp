from django import forms
from .models import Director, Film, Review


class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = '__all__'


class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))

    class Meta:
        model = Review
        fields = '__all__'
