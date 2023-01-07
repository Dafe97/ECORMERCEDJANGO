from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True )
    description = models.TextField(max_length=50,null=True, blank=True )
    price = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(default=0, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True )

    def __str__(self):
        return f"{self.id} :{self.name}"

class Image(models.Model):
    name = models.ImageField(null=True, blank=True, upload_to='products/images')
    products = models.ForeignKey('Product',on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.id} :{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=45, null=False, blank=False, unique=True)
    image = models.ImageField(null= True, blank=True, upload_to="Images/categories/")
    parent = models.ForeignKey('Category',null=True, related_name="subcategories",on_delete=models.SET_NULL)
    def __str__(self) -> str:
        return f" {self.id}: {self.name}"