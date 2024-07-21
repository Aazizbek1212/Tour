from django.urls import path



from apps.bookings.views import create_booking


urlpatterns = [
    path('new/<int:pk>/', create_booking, name='create_booking'),
]
