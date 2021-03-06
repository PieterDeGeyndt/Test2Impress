from django.db import models
from django.utils import timezone
from datetime import date

class Pasttest(models.Model):
    testimg = models.ImageField(upload_to="pasttestmedia/projimage/",default="")
    testtitle = models.CharField(max_length=200,default="")
    teststart = models.DateField(default=timezone.now)
    testend = models.DateField(default=timezone.now)
    testbody = models.TextField(default="") 
    testquotes = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.testtitle
    
    def yearstart(self):
        return self.teststart.strftime('%Y')
    
    def startddmmyy(self):
        return self.teststart.strftime('%d %b %Y')
    
    def endddmmyy(self):
        return self.testend.strftime('%d %b %Y')
    
    @property
    def is_past_now(self):
        return date.today() < self.testend
    