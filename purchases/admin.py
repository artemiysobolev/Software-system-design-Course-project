from django.contrib import admin
from .models import *


class ExcursionInPurchaseInline (admin.TabularInline):
    model = ExcursionInPurchase
    extra = 0


class PurchaseAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Purchase._meta.fields]
    inlines = [ExcursionInPurchaseInline]

    class Meta:
        model = Purchase


admin.site.register(Purchase, PurchaseAdmin)


class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class ExcursionInPurchaseAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ExcursionInPurchase._meta.fields]

    class Meta:
        model = ExcursionInPurchase


admin.site.register(ExcursionInPurchase, ExcursionInPurchaseAdmin)



class   ExcursionInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ExcursionInBasket._meta.fields]

    class Meta:
        model: ExcursionInBasket


admin.site.register(ExcursionInBasket, ExcursionInBasketAdmin)