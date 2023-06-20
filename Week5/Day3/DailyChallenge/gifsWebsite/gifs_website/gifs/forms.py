from django import forms
from .models import Gif, Category


class GifForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Gif
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
            }),
            'url': forms.URLInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'URL'
            }),
            'uploader_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Uploader Name'
            }),
            'categories': forms.MultipleChoiceField(),
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ['gifs']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
            }),
        }
        # fields = '__all__'
