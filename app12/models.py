from email.policy import default
from pyexpat import model


from django.db import models




# Create your models here.
class listing(models.Model):
    title = models.CharField(max_length=100)
    Description = models.CharField(max_length=3000)
    app_url = models.CharField(max_length=2000)
    date_app = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title

