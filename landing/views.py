from django.shortcuts import render
from .forms import SubscriberForm
from excursions.models import *

def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
    excursions_images = ExcursionImage.objects.filter(is_active=True,is_main=True, excursion__is_active=True)
    excursions_images_churches = excursions_images.filter(excursion__category__id=1)
    excursions_images_panoramas = excursions_images.filter(excursion__category__id=2)
    excursions_images_russia = excursions_images.filter(excursion__category__id=3)
    return render(request, 'landing/home.html', locals())
