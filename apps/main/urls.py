from django.urls import path

from apps.main.views import DestinationList, countries_view, detail_view, home_view, tours, tours2_view


urlpatterns = [
    path('', home_view, name='home'),
    path('destination/', DestinationList.as_view(), name='list'),
    path('countrys/', countries_view, name='davlatlar'),
    path('sayohatlar/<int:pk>/', tours2_view, name='sayohatlar'),
    path('detail/<int:pk>/', detail_view, name='detailtour'),
    path('toursall/', tours, name='alltours'),

]
