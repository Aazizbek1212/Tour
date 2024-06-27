from django.db import models


class Tour(models.Model):
        state_name = models.CharField(max_length=100)
        imgae = models.ImageField(blank=True, null=True)
        travel_time = models.IntegerField()
        description = models.TextField()
