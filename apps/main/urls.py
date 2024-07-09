from django.urls import path

from apps.main.views import DestinationList, countries_view, country_view, detail_view,  main_view, tours2_view


urlpatterns = [
    path('', main_view, name='home'),
    path('destination/', DestinationList.as_view(), name='list'),
    path('countrys/', countries_view, name='davlatlar'),
    path('tours/<int:pk>/', country_view, name='tours'),
    path('sayohatlar/<int:pk>/', tours2_view, name='sayohatlar'),
    path('detail/<int:pk>/', detail_view, name='detailtour'),

]
