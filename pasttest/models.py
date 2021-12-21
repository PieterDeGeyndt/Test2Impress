from django.db import models
from django.utils import timezone

class Pasttest(models.Model):
    testimg = models.ImageField(verbose_name='Project Image', upload_to="pasttestmedia/projimage/",default="")
    testtitle = models.CharField(max_length=200, verbose_name='Project Title',default="")
    teststart = models.DateField(verbose_name='Project Start', default=timezone.now)
    testend = models.DateField(verbose_name='Project End', default=timezone.now)
    testbody = models.TextField(verbose_name='Project Body', default="") 
    testquotes = models.TextField(verbose_name='Project Quotes', default="")

    def __str__(self):
        return self.testtitle