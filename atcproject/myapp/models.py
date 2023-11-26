from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_doctor = models.BooleanField('Is customer', default=False)
    is_patient = models.BooleanField('Is employee', default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    

    
    def __str__(self):
        return self.username