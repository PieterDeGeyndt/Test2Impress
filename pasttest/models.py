from django.db import models

class Pasttest(models.Model):
    testimg = models.ImageField(verbose_name='Project Image', upload_to="pasttestmedia/projimage/")
    testtitle = models.CharField(max_length=200, verbose_name='Project Title')
    teststart = models.DateField(verbose_name='Project Start')
    testend = models.DateField(verbose_name='Project End')
    testbody = models.TextField(verbose_name='Project Body') 
    testquotes = models.TextField(verbose_name='Project Quotes')

    def __str__(self):
        return self.testtitle