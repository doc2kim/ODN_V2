from django.db import models

# Create your models here.

class Buoy(models.Model):
    buoy_id = models.IntegerField(primary_key=True)
    voltage = models.IntegerField(null=True)
    
    def __str__(self):
            return '{}'.format(self.buoy_id)

class Location(models.Model):
    buoy = models.ForeignKey(Buoy, related_name='location_buoy', on_delete=models.PROTECT)
    lat = models.FloatField()
    lon = models.FloatField()
    
    def buoy_id(self):
        return self.buoy.buoy_id
    
    def __str__(self):
            return '{}, {}'.format(self.lat, self.lon)
    
    
class Data(models.Model):
    location = models.ForeignKey(Location, related_name='data_location', on_delete=models.PROTECT)
    temp = models.FloatField()
    oxy = models.FloatField()
    ph = models.FloatField()
    ppt = models.FloatField()
    orp = models.IntegerField()
    o4e = models.IntegerField()
    crc = models.CharField(max_length = 100)
    date = models.DateField()
    time = models.TimeField()
    
    def buoy_id(self):
        return self.location.buoy
    
    def __str__(self):
            return '{}'.format(self.location)
    



    
    
    