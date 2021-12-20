from django.db import models

class Pastweb(models.Model):
    webimg = models.ImageField(verbose_name='Website Image', upload_to="pastwebmedia/webimg/",default="")
    webtitle = models.CharField(max_length=200, verbose_name='Website Title',default="")
    webbody = models.TextField(verbose_name='Website Body', default="")
    weburl = models.URLField(verbose_name='Website Url', default="")

    def __str__(self):
        return self.webtitle