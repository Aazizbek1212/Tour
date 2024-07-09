from django.contrib import admin

from apps.tour.models import Country, Destination, Tour



admin.site.register(Country)
admin.site.register(Destination)
admin.site.register(Tour)