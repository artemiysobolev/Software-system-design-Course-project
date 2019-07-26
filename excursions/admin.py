from django.contrib import admin
from .models import *


class ExcursionCategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ExcursionCategory._meta.fields]

    class Meta:
        model = ExcursionCategory


admin.site.register(ExcursionCategory, ExcursionCategoryAdmin)

class ExcursionImageInline (admin.TabularInline):
    model = ExcursionImage
    extra = 0

class ExcursionAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Excursion._meta.fields]
    inlines = [ExcursionImageInline]

    class Meta:
        model = Excursion


admin.site.register(Excursion, ExcursionAdmin)


class ExcursionImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ExcursionImage._meta.fields]

    class Meta:
        model = ExcursionImage


admin.site.register(ExcursionImage, ExcursionImageAdmin)