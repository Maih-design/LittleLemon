from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField()
    BookingDate = models.DateField()
    
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
