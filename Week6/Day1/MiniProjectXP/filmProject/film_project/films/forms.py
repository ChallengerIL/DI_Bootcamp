from django import forms
from .models import Director, Film


class AddFilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = '__all__'


class AddDirectorForm(forms.ModelForm):
    # films = forms.ModelChoiceField(queryset=Film.objects.all())

    class Meta:
        model = Director
        fields = '__all__'
        # widgets = {
        #     'films': forms.ChoiceField(),
        # }
