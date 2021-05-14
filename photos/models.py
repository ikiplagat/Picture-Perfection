from django.db import models
from django.forms.fields import ImageField

class Category(models.Model):
  name = models.CharField(max_length =30)

  def __str__(self):
      return self.name
    
class Location(models.Model):  
  name = models.CharField(max_length =30)

  def __str__(self):
      return self.name  
    
class Image(models.Model):
  image = models.ImageField(upload_to = 'images/')
  name = models.CharField(max_length =30)
  description = models.CharField(max_length =60)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  
  def __str__(self):
      return self.name
    
  def save_image(self):
      self.save()
      
  @classmethod
  def search_by_category(cls, search_term):
    photos = cls.objects.filter(category__name__contains=search_term) 
    return photos   
  
  @classmethod
  def search_by_location(cls, search_term):
    photos = cls.objects.filter(location__name__contains=search_term) 
    return photos  
 