from django.db import models

# Create your models here.

class Mock_db(models.Model):
    name = models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    stack=models.CharField(max_length=20)
    team_lead=models.CharField(max_length=20)
   
    def __str__(self):
        return self.name
