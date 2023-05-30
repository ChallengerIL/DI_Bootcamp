from django.shortcuts import render, redirect
from .models import Person
from .forms import PhoneForm


# http://127.0.0.1:8000/persons/name/Haim/
def name(request, persons_name):
    try:
        person = Person.objects.get(name=persons_name.title())
    except Person.DoesNotExist:
        person = None

    context = {
        'person': person,
    }
    return render(request, 'information/name.html', context)


# http://127.0.0.1:8000/persons/phonenumber/+97237510290/
def phone_number(request, phone):
    try:
        person = Person.objects.get(phone_number=phone)
    except Person.DoesNotExist:
        person = None

    context = {
        'person': person,
    }
    return render(request, 'information/phone_number.html', context)


def search(request):
    if request.method == "POST":
        query = request.POST['search']

        if PhoneForm({"number": query}).is_valid():
            return redirect('phone_number', phone=query)
        else:
            return redirect('name', persons_name=query)

    return render(request, 'information/index.html')


# Phone numbers and names
# +97236834420 Sarit
# +97237510290 Haim
# +97248335242 Marganita
