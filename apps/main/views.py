from django.shortcuts import render
from django.views.generic import ListView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.main.serializers import TourSerializer

from apps.tour.models import Country, Destination, Tour




def main_view(request):
    tour = Tour.objects.all()[:4]
    return render(request , 'index.html', {'tour':tour})




class DestinationList(ListView):
    model = Destination
    template_name = 'list.html'
    context_object_name = 'destinations'




def country_view(request, pk):
    country = Country.objects.get(id=pk)
    destinations = country.destination_set.all()
    # tour = Tour.objects.filter(destinations=destination)

    return render(request, 'tours.html', {'country':country, 'destinations':destinations})


def countries_view(request):
    countries = Country.objects.all()
    return render(request, 'countries.html',{'countries':countries})




def tours2_view(request, pk):
    destinations = Destination.objects.get(id=pk)
    sayohatlar = destinations.tour_set.all()
    return render(request, 'tours2.html', {'destinations':destinations, 'sayohatlar':sayohatlar})



def detail_view(request, pk):
    sayohat = Tour.objects.get(id=pk)

    return render(request, 'detail.html', {'sayohat':sayohat})







@api_view(['GET'])  
def tours(request, pk):
    try:
        destination = Destination.objects.get(id=pk)
        tours = destination.tours.all()
        data = TourSerializer(tours, many=True).data
        return Response({'tours': data})
    except Destination.DoesNotExist:
        return Response({'error': 'Destination not found'}, status=404)
