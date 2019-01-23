from django.db import models

# Create your models here.

class weka_entry(models.Model):
    pelvic_incidence = models.FloatField()
    pelvic_tilt = models.FloatField()
    lumbar_lordosis_angle = models.FloatField()
    sacral_slope = models.FloatField()
    pelvic_radius = models.FloatField()
    degree_spondylolisthesis = models.FloatField()
    weka_class = models.CharField(max_length="100")


# class CSVTable(models.Model):
#     title = models.CharField(max_length=128, default='Table')
#
#
# class Line(models.Model):
#     lineNumber = models.IntegerField()
#     belonging_table = models.ForeignKey(CSVTable, on_delete=models.CASCADE)
#
# class Entry(models.Model):
#     entry = models.CharField(max_length=32)
#     beloning_line = models.ForeignKey(Line, on_delete=models.CASCADE)



