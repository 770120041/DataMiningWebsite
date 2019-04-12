from django.db import models

# import this module to serilize dataframez
from django.urls import  reverse
# Create your models here.


class DataFrameModel(models.Model):
    df_description = models.CharField(max_length = 150)
    df_stroed_name = models.CharField(max_length = 150, blank="null")

    def df_path(self):
        return u'{data_path}'.format(data_path=self.df_stroed_name)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('csv-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.df_description



