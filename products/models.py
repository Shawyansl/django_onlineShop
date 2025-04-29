from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE , related_name="children")

class Discount(models.Model):
    CHOICES = ( (1, "CASH") , (2, "PERCENT") )
    discount_type = models.SmallIntegerField(default=1 , choices= CHOICES)
    amount = models.PositiveIntegerField()
    max_amount = models.PositiveIntegerField(blank=True , null=True)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sku = models.CharField(max_length=100 , unique= True)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="products")
    qty = models.PositiveIntegerField(default=1)
    discount = models.ForeignKey(Discount , on_delete=models.CASCADE , related_name="products" , blank=True , null=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name="reviews")
    body = models.TextField(default="")
    rate = models.SmallIntegerField(default=1)
    user = models.ForeignKey("accounts.User" , on_delete=models.CASCADE , related_name="users")

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name="details")
    key = models.CharField(max_length=50)
    value = models.TextField()

class ProductImage(models.Model):
    image_file = models.ImageField(upload_to="product_images")
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name="images")
