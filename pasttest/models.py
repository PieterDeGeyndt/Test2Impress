from django.db import models

class Pasttest(models.Model):
    testimg = models.ImageField(name='Project Image', upload_to="pasttestmedia/projimage/")
    testtitle = models.CharField(max_length=200, name='Project Title')
    teststart = models.DateField(name='Project Start')
    testend = models.DateField(name='Project End')
    testbody = models.TextField(name='Project Body') 
    testquotes = models.TextField(name='Project Quotes')

    def __str__(self):
        return self.testtitle