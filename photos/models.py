from django.db import models
from django.forms.fields import ImageField
from cloudinary.models import CloudinaryField

class Category(models.Model):
  name = models.CharField(max_length =30)

  def __str__(self):
      return self.name
    
  def save_category(self):
      self.save() 
      
  @classmethod
  def update_category(cls,id,name):
    cls.objects.filter(id=id).update(name=name)     
      
  def delete_category(self):
      self.delete()     
    
class Location(models.Model):  
  name = models.CharField(max_length =30)

  def __str__(self):
      return self.name 
    
  def save_location(self):
      self.save()  
      
  @classmethod
  def update_location(cls,id,name):
    cls.objects.filter(id=id).update(name=name)     
      
  def delete_location(self):
    self.delete()       
    
class Image(models.Model):
  image = CloudinaryField('photo')
  name = models.CharField(max_length =30)
  description = models.CharField(max_length =60)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  
  def __str__(self):
      return self.name
    
  def save_image(self):
      self.save()
      
  def delete_image(self):
    self.delete()  
    
  @classmethod
  def get_image_by_id(cls,id):
    image=cls.objects.get(id=id)
    return image    
      
  @classmethod
  def search_by_category(cls, search_term):
    photos = cls.objects.filter(category__name__contains=search_term) 
    return photos   
  
  @classmethod
  def search_by_location(cls, search_term):
    photos = cls.objects.filter(location__name__contains=search_term) 
    return photos  
 