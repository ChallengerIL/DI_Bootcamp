from django import forms
from django.db import models


class DateInput(forms.DateInput):
    input_type = 'date'


class Todo(models.Model):

    title = models.CharField(max_length=100)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateField(blank=True, null=True)
    deadline_date = models.DateField()

    def __str__(self):
        return self.title


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
