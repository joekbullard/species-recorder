from django.contrib.gis.db import models


        

class Recorder(models.Model):
    recorder_id = models.AutoField(primary_key=True)
    recorder_user = models.CharField(max_length=20, blank=True, null=True)
    recorder_first_name = models.CharField(max_length=20, blank=True, null=True)
    recorder_last_name = models.CharField(max_length=30, blank=True, null=True)
    recorder_email = models.CharField(max_length=100, blank=True, null=True)
    recorder_join_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.recorder_user
    
    class Meta:
        verbose_name = 'recorder'


class Records(models.Model):
    record_id = models.AutoField(primary_key=True)
    recorder = models.ForeignKey(Recorder, models.DO_NOTHING, db_column='recorder', blank=True, null=True)
    species = models.TextField(max_length=100, blank=False, null=False)
    record_date = models.DateField()
    notes = models.CharField(max_length=255, blank=True, null=True)
    geom = models.PointField(srid=27700)

    def __int__(self):
        return self.record_id

    class Meta:
        verbose_name = 'record'




