from django import forms
from .models import Director, Producer, Film, Review
from django.forms import formset_factory


class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        exclude = ['producers']


class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = '__all__'


class ProducerForm(forms.ModelForm):

    class Meta:
        model = Producer
        fields = '__all__'


ProducerFormSet = formset_factory(ProducerForm, extra=2)


class ReviewForm(forms.ModelForm):
    CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))

    class Meta:
        model = Review
        fields = '__all__'
