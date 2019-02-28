from django.db import models

# import this module to serilize dataframez
# from picklefield.fields import PickledObjectField
from django.urls import  reverse
# Create your models here.


class DataFrameModel(models.Model):
    data_frame_name = models.CharField(max_length = 150)
    data_frame_path = models.CharField(max_length = 150, blank="null")
    #
    def df_path(self):
        return u'{data_path}'.format(data_path=self.data_frame_path)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('csv-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.data_frame_name


