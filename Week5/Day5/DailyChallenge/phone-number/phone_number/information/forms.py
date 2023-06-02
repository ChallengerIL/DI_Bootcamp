from django import forms
from phonenumber_field.formfields import PhoneNumberField


class PhoneForm(forms.ModelForm):
    phone_number = PhoneNumberField(region="IL")
