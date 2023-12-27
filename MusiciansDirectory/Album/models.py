from django.db import models
from Musician.models import Musician
# Create your models here.

class Album(models.Model):
   rating_choice=[
      (1,'One'),
      (2,'Two'),
      (3,'Three'),
      (4,'Four'),
      (5,'Five'),
   ]
   Name=models.CharField(max_length=100,unique=True)
   MusicianList=models.ForeignKey(to=Musician, on_delete=models.CASCADE)
   ReleaseDate=models.DateField()
   Rating=models.IntegerField(choices=rating_choice)

   def __str__(self) -> str:
      return self.Name

   

