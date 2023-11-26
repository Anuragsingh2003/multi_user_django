from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('doc_login/', views.doctor_login, name='doctor_login'),
    path('doctor/', views.doctor, name='doctor'),
    path('patient/', views.patient, name='patient'),
    path('logt/', views.logt, name='logt'),
    path('patient_login/', views.patient_login, name='patient_login'),
    
]
