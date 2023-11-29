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
    path('create_blog_post/', views.create_blog_post, name='create_blog_post'),
    path('my_posts/',  views.my_posts, name='my_posts'),
    path('view_blog_posts/',  views.view_blog_posts, name='view_blog_posts'),
    path('view_blog_posts/<str:category_name>/',  views.view_blog_posts, name='view_blog_posts_by_category'),


    
]
