
from django.db import models
from apps.main.models import BaseModel, Image

from ckeditor.fields import RichTextField


class Country(BaseModel):
    namee = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/countries/')

    def __str__(self):
        return self.namee


class Destination(BaseModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/destinations/')
    country = models.ForeignKey(
        Country, models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-id' ,)
    
    @property
    def lowest_price(self):
        try:
            tours = self.tours.order_by('price')
            return tours.first().price
        except:
            return 0


class Category(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
   

class Ingredient(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class HotelFacility(BaseModel):
    name = models.CharField(max_length=200)


class Hotel(BaseModel):
    name = models.CharField(max_length=200)
    stars = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/hotels/')
    description = RichTextField(blank=True, null=True)
    facilities = models.ManyToManyField(HotelFacility, blank=True)
    hotel_class = models.CharField(max_length=100, blank=True, null=True)
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.name


class Tour(BaseModel):
    name = models.CharField(max_length=250)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='images/tours/')
    destinations = models.ManyToManyField(Destination, blank=True)
    countries = models.ManyToManyField(Country, blank=True)
    categories = models.ManyToManyField(Category , blank=True)
    hotels = models.ManyToManyField(Hotel, blank=True)
    count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name


class Review(BaseModel):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=200, blank=True, null=True)
    report = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(blank=True, null=True)
    tours = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)

    def __str__(self):
        return self.name


class Food(BaseModel):
    has_breakfast = models.BooleanField(default=True)
    has_lunch = models.BooleanField(default=False)
    has_dinner = models.BooleanField(default=False)

    breakfast = models.TextField(blank=True, null=True)
    lunch = models.TextField(blank=True, null=True)
    dinner = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE, related_name='food', blank=True, null=True)









