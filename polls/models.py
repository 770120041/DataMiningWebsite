from django.db import models

# Create your models here.


class CSVTable(models.Model):
    title = models.CharField(max_length=128, default='Table')


class Line(models.Model):
    lineNumber = models.IntegerField()
    belonging_table = models.ForeignKey(CSVTable, on_delete=models.CASCADE)

class Entry(models.Model):
    entry = models.CharField(max_length=32)
    beloning_line = models.ForeignKey(Line, on_delete=models.CASCADE)



