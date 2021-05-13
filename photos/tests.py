from django.test import TestCase
from .models import Category, Image, Location

class CategoryTestClass(TestCase):
   # Set up method
    def setUp(self):
      self.image = Category(name = 'travel')
      
   # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Category))  
        

class LocationTestClass(TestCase):
   # Set up method
    def setUp(self):
      self.location = Location(name = 'Dubai')
      
   # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location)) 
        
        
class ImageTestClass(TestCase):
   # Set up method
    def setUp(self):
      self.category = Category(name = 'travel')
      self.category.save()
      self.location = Location(name = 'Dubai')
      self.location.save()
      self.image = Image(name = 'image_name', description = 'this is an image', category = self.category, location = self.location)
      
   # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image)) 
        
    def test_save_method(self):
      self.image.save()     
      images = Image.objects.all()
      self.assertTrue(len(images) > 0) 
      
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()  
