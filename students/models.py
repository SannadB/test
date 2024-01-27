from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  active = models.BooleanField(default=True)
  profile_image = models.ImageField(upload_to="profile_images", blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products", blank=True, null=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_file = models.ImageField(upload_to="items", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Rating(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField()