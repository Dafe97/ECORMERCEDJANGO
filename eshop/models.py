from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True )
    description = models.TextField(max_length=50,null=True, blank=True )
    price = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(default=0, null=True, blank=True )
    Category = models.ForeignKey('Category',null=True,blank=False,on_delete=models.SET_NULL,related_name='products')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True )

    def __str__(self):
        return f"{self.id} :{self.name}"
    
    @property
    def first_image(self):
        if self.images.all():
            return self.images.all()[0].name.url
        else:
            return ''
            

class Image(models.Model):
    name = models.ImageField(null=True, blank=True, upload_to='images/products')
    products = models.ForeignKey('Product',on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.id} :{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=45, null=False, blank=False, unique=True)
    image = models.ImageField(null= True, blank=True, upload_to="images/categories/")
    parent = models.ForeignKey('Category',null=True, related_name="subcategories",on_delete=models.SET_NULL,blank=True)
    def __str__(self) -> str:
        return f" {self.id}: {self.name}"