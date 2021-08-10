from django.urls import path
from.import views

urlpatterns = [
    path('second/', views.second_page),
    path('example/', views.example),
    path('', views.landing_page),
]
