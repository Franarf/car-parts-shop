from django.db import models
from datetime import datetime


# Create your models here.
 
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    user_id = models.IntegerField(blank=True)
    customer_need = models.CharField(max_length=100)
    title_car = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    
    create_date = models.DateTimeField(blank=True, default=datetime.now)


    # def car_id(self):
    #     return self.car_id
    # car_id.short_description = 'Macchina'

    def __str__(self):
        return self.email
