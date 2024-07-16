from django.urls import path

from apps.main.views import DestinationList, ToursView, countries_view, detail_view, home_view, hotel_view,  tours2_view


urlpatterns = [
    path('', home_view, name='home'),
    path('destination/', DestinationList.as_view(), name='list'),
    path('countries/', countries_view, name='davlatlar'),
    path('sayohatlar/<int:pk>/', tours2_view, name='sayohatlar'),
    path('detail/<int:pk>/', detail_view, name='detailtour'),
    path('toursall/', ToursView.as_view(), name='alltours'),
    path('detail-hotel/<int:pk>/', hotel_view, name='hotel')
    

]
