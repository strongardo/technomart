from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products', null=True)
    old_price = models.IntegerField(default=0)
    is_hit = models.BooleanField(default=False)
    manufacturer = models.CharField(max_length=30, default="BOSCH")

    def __str__(self):
        return self.name