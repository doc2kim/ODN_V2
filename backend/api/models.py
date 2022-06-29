from django.db import models

# Create your models here.


class Opendata(models.Model):
    id = models.AutoField(primary_key=True)
    ocean = models.CharField(max_length=80, default="none")
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    area1 = models.CharField(max_length=80, null=True)
    area2 = models.CharField(max_length=80, null=True)
    area3 = models.CharField(max_length=80, null=True)
    area4 = models.CharField(max_length=80, null=True)
    temp = models.FloatField(default=0)
    oxy = models.FloatField(default=0)
    ph = models.FloatField(default=0)
    salt = models.FloatField(default=0)
    ntu = models.FloatField(default=0)
    obs_date = models.DateField()
    obs_time = models.TimeField()

    def __str__(self):
        return self.area3
