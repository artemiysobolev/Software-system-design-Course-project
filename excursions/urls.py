from django.conf.urls import url, include
from django.contrib import admin
from excursions import views

urlpatterns = [
    # url(r'^landing/', views.landing, name="landing")
    url(r'^excursion/(?P<excursion_id>\w+)/$', views.excursion, name='excursion')
]

