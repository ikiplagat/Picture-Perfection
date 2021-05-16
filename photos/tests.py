from django.test import TestCase
from .models import Category, Image, Location

class CategoryTestClass(TestCase):
   # Set up method
   def setUp(self):
      self.category = Category(name = 'travel')
      
   # Testing  instance
   def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))    
        
   def test_save_method(self):
      self.category.save_category()     
      categories = Category.objects.all()
      self.assertTrue(len(categories) > 0) 
      
   def test_update_category(self):
      self.category.save_category()
      self.category.update_category(self.category.id,'fitness')
      update=Category.objects.get(name='fitness')
      self.assertEqual(update.name,'fitness')       
      
   def tearDown(self):
        Category.objects.all().delete()  
        
   def test_delete_category(self):
      self.category.save_category()
      categories=Category.objects.all()
      self.assertEqual(len(categories),1)
      self.category.delete_category()
      del_category=Category.objects.all()
      self.assertEqual(len(del_category),0) 
        

class LocationTestClass(TestCase):
   # Set up method
   def setUp(self):
      self.location = Location(name = 'Dubai')
      
   # Testing  instance
   def test_instance(self):
        self.assertTrue(isinstance(self.location,Location)) 
        
   def test_save_method(self):
      self.location.save_location()     
      locations = Location.objects.all()
      self.assertTrue(len(locations) > 0)
      
   def test_update_location(self):
      self.location.save_location()
      self.location.update_location(self.location.id,'Dubai')
      update=Location.objects.get(name='Dubai')
      self.assertEqual(update.name,'Dubai')     
      
   def tearDown(self):
        Location.objects.all().delete() 
        
   def test_delete_location(self):
    self.location.save_location()
    locations=Location.objects.all()
    self.assertEqual(len(locations),1)
    self.location.delete_location()
    del_location=Location.objects.all()
    self.assertEqual(len(del_location),0)              
        
        
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
      Image.objects.all().delete() 
      Category.objects.all().delete() 
      Location.objects.all().delete() 
        
   def test_delete_image(self):
      self.image.save_image()
      images=Image.objects.all()
      self.assertEqual(len(images),1)
      self.image.delete_image()
      del_images=Image.objects.all()
      self.assertEqual(len(del_images),0)   
    
   def test_search_category(self):
      self.location = Location(name='Nairobi')
      self.location.save_location()
      self.category = Category(name='fitness')
      self.category.save_category()
      self.image=Image(image="photo.png",name='gym',description='workout',location=self.location,category=self.category)
      self.image.save_image()
      images=Image.search_by_category(self.category.name)
      self.assertEqual(len(images),1)              
       
   def test_get_image_by_id(self):
      self.location = Location(name='Nairobi')
      self.location.save_location()
      self.category = Category(name='fitness')
      self.category.save_category()
      self.image= Image(id=1,image="photo.png",name='gym',description='workout',location=self.location,category=self.category)
      self.image.save_image()
      images = Image.get_image_by_id(self.image.id)
      self.assertEqual(images.name, self.image.name) 
    
   def test_search_location(self):
      self.location = Location(name='Nairobi')
      self.location.save_location()
      self.category = Category(name='fitness')
      self.category.save_category()
      self.image=Image(id=1,image="photo.png",name='gym',description='workout',location=self.location,category=self.category)
      self.image.save_image()
      images = Image.search_by_location("Nairobi")
      self.assertTrue(len(images) > 0) 
