from django.contrib import admin

from apps.tour.models import Category, Country, Destination, Tour



admin.site.register(Country)
admin.site.register(Destination)
admin.site.register(Tour)
admin.site.register(Category)