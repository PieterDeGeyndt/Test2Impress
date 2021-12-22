from django.db import models
from django.utils import timezone

class Pasttest(models.Model):
    testimg = models.ImageField(upload_to="pasttestmedia/projimage/",default="")
    testtitle = models.CharField(max_length=200,default="")
    teststart = models.DateField(default=timezone.now)
    testend = models.DateField(default=timezone.now)
    testbody = models.TextField(default="") 
    testquotes = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.testtitle
    
    def get_year(self):
        date=Pasttest.teststart.date()
        year=date[:4]
        return year
        