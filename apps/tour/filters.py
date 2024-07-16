from django_filters import FilterSet

from apps.tour.models import Tour



class TourFilter(FilterSet):

    class Meta:
        model = Tour
        fields = {'name':['contains'], 'price':['lte'], 'categories':['exact'],'countries':['exact'], 'destinations':['exact']}