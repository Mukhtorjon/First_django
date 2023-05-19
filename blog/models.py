from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    aftor=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="Media/img",null=True,blank=True)
    text=models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("home")