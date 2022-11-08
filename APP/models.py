from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user(models.Model):
    name = models.CharField(max_length = 128)
    email = models.EmailField(max_length = 128,unique=True)
    password = models.CharField(max_length = 128)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portofolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__ (self):
        return self.user.username