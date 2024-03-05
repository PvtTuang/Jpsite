from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_type = models.CharField(
    max_length=10,
    choices=[('owner', 'Owner'), ('customer', 'Customer')],
    default='customer'
    )

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10,choices=[
        ('owner', 'Owner'),
        ('customer', 'Customer')])

    def __str__(self) -> str:
        return self.user 