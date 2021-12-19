from django.db import models

class Pastweb(models.Model):
    webimg = models.ImageField(name='Website Image', upload_to="pastwebmedia/webimg/")
    webtitle = models.CharField(max_length=200, name='Website Title')
    webbody = models.TextField(name='Website Body')
    weburl = models.URLField(name='Website Url')

    def __str__(self):
        return self.webtitle