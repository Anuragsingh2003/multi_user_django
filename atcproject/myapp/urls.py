from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('doctor/', views.doctor, name='doctor'),
    path('patient/', views.patient, name='patient'),
]
