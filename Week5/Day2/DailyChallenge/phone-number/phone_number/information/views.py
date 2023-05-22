from django.shortcuts import render
from .models import Person


# http://127.0.0.1:8000/persons/name/Haim%20Uriel/
def name(request, persons_name):
    context = {
        'person': Person.objects.get(name=persons_name),
    }
    return render(request, 'information/name.html', context)


# http://127.0.0.1:8000/persons/phonenumber/+97237510290/
def phone_number(request, phone):
    context = {
        'person': Person.objects.get(phone_number=phone),
    }
    return render(request, 'information/phone_number.html', context)


# Phone numbers and names
# +97236834420 Sarit Yosef
# +97237510290 Haim Uriel
# +97248335242 Marganita Yocheved
