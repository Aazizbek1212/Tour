from django.shortcuts import render
from django.views.generic import ListView

from rest_framework.decorators import api_view
from django_filters.views import FilterView
from rest_framework.response import Response
from apps.main.serializers import TourSerializer

from apps.tour.filters import TourFilter
from apps.tour.models import Category, Country, Destination, Food, Hotel, Tour




def home_view(request):

    destinations = Destination.objects.all()[:2]
    destinations2 = Destination.objects.all()[2:3].first()
    tour = Tour.objects.all()[:5]
    category  = Category.objects.all()
    return render(request , 'index.html', {'tour':tour, 'destinations':destinations,'destinations2':destinations2, 'category':category })
    




class DestinationList(ListView):
    model = Destination
    template_name = 'list.html'
    context_object_name = 'destinations'







def countries_view(request):
    countries = Country.objects.all()
    return render(request, 'countries.html',{'countries':countries})




def tours2_view(request, pk):
    destinations = Destination.objects.get(id=pk)
    sayohatlar = destinations.tour_set.all()
    return render(request, 'tours2.html', {'destinations':destinations, 'sayohatlar':sayohatlar})





def detail_view(request, pk):
    sayohat = Tour.objects.get(id=pk)
    sayohat.count += 1
    sayohat.save()
    return render(request, 'detail.html', {'sayohat':sayohat})











class ToursView(FilterView):
    model = Tour
    template_name = 'alltours.html'
    context_object_name = 'tours'
    filterset_class = TourFilter

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('tourSearch', None)
        
        if search:
            qs = qs.filter(name__contains=search)
        return qs


        
    


def hotel_view(request, pk):
    hotel = Hotel.objects.get(id=pk)
    return render(request, 'hotel_detail.html', {'hotel':hotel})





@api_view(['GET'])  
def tours(request, pk):
    try:
        destination = Destination.objects.get(id=pk)
        tours = destination.tours.all()
        data = TourSerializer(tours, many=True).data
        return Response({'tours': data})
    except Destination.DoesNotExist:
        return Response({'error': 'Destination not found'}, status=404)
