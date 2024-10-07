from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    have = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    video = models.ImageField(upload_to='vid/', null=True, blank=True)


    def __str__(self):
        return self.product_name


