from django.shortcuts import render
from excursions.models import *


def excursion(request, excursion_id):
    excursion =  Excursion.objects.get(id=excursion_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'excursions/excursion.html', locals())