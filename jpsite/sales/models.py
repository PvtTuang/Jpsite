from django.db import models
from posts.models import Product

# Create your models here.

class Sale(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_date = models.DateField(auto_now_add = True)

    def total_price(self):
        return self.product.price * self.quantity