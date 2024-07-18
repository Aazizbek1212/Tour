from django.contrib import admin

from apps.tour.models import Category, Country, Destination, Food, Ingredient, Review, Tour, Hotel, HotelFacility



admin.site.register(Country)
admin.site.register(Destination)
admin.site.register(Tour)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(Hotel)
admin.site.register(HotelFacility)
admin.site.register(Review)