from django import forms
from .models import Todo


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        exclude = ['has_been_done', 'date_creation', 'date_completion']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
            }),
            'details': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Details'
            }),
            'deadline_date': DateInput(),
        }
