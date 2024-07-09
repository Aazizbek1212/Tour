from rest_framework import serializers

from apps.tour.models import Tour


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'



