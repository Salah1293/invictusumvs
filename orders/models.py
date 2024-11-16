from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import Profile
from products.models import Robot
from services.models import Mission
# Create your models here.


class Order(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    name = models.CharField(max_length=200, null=False, blank=False) 
    company_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order by {self.profile.name}'
    
    class Meta:
        db_table = 'Order'
    

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Robot, null=True, blank=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Mission, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Item {self.id} for Order {self.id}'
    
    class Meta:
        db_table = 'OrderItem'