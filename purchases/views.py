from django.http import JsonResponse
from .models import ExcursionInBasket


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    excursion_id = data.get("excursion_id")

    new_excursion = ExcursionInBasket.objects.create(session_key=session_key, excursion_id=excursion_id)
    excursion_total_nmb = ExcursionInBasket.objects.filter(session_key=session_key, is_active= True).count()
    return_dict["excurstion_nubmer"] = excursion_total_nmb
    return JsonResponse(return_dict)