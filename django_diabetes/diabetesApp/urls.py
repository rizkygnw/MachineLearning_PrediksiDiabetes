from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Halaman utama dengan form input
    path('result', views.forminfo, name='forminfo'),  # Halaman hasil prediksi
]
