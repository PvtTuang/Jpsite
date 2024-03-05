from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    COMPUTER = 'Computer'
    LAPTOP = 'Laptop'
    COMPUTER_ACCESSORY = 'Computer Accessory'
    SPEAKER = 'Speaker'

    CATEGORY_CHOICES = [
        (COMPUTER, 'คอมพิวเตอร์'),
        (LAPTOP, 'โน๊ตบุ๊ค'),
        (COMPUTER_ACCESSORY, 'อุปกรณ์คอมพิวเตอร์'),
        (SPEAKER, 'ลำโพง'),
    ]

    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    timestamp = models.DateTimeField(default=timezone.now)
    quantity = models.PositiveIntegerField(default = 0)
    image1 = models.ImageField(upload_to='static/product_images/')
    image2 = models.ImageField(upload_to='static/product_images/', blank=True)
    image3 = models.ImageField(upload_to='static/product_images/', blank=True)

    def __str__(self):
        return self.name
 