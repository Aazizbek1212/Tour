from django.shortcuts import render, redirect

from apps.bookings.models import Booking
from apps.tour.models import Tour


def create_booking(request, pk):
    tour = Tour.objects.filter(id=pk).first()
    adult_count = request.POST.get('adult_count')
    print(adult_count)
    kid_count = request.POST.get('kid_count')
    pet_count = request.POST.get('pet_count')
    booking = Booking.objects.create(
        tour=tour, adult_count=adult_count, kid_count=kid_count, pet_count=pet_count)
    if request.user.is_authenticated:
        booking.user = request.user
        booking.save()
    return redirect('detailtour', pk)


