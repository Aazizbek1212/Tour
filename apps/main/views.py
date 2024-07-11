from django.shortcuts import render
from django.views.generic import ListView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.main.serializers import TourSerializer

from apps.tour.models import Country, Destination, Tour




def home_view(request):

    destinations = Destination.objects.all()[:2]
    destinations2 = Destination.objects.all()[2:3].first()
    tour = Tour.objects.all()[:5]
    return render(request , 'index.html', {'tour':tour, 'destinations':destinations,'destinations2':destinations2 })
    




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




# class ToursList(ListView):
#     model = Tour
#     template_name = 'alltours.html'
#     context_object_name = 'tour'


def tours(request):
    query = request.GET.get('tourSearch')
    tour = Tour.objects.all()
    if query:
        tour = tour.filter(name__icontains=query)

    return render(request, 'alltours.html', {'tour':tour})    









@api_view(['GET'])  
def tours(request, pk):
    try:
        destination = Destination.objects.get(id=pk)
        tours = destination.tours.all()
        data = TourSerializer(tours, many=True).data
        return Response({'tours': data})
    except Destination.DoesNotExist:
        return Response({'error': 'Destination not found'}, status=404)
