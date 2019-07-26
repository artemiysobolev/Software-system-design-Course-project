from .models import ExcursionInBasket

def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    excursions_total_nmb = ExcursionInBasket.objects.filter(session_key=session_key, is_active= True).count()

    return locals()