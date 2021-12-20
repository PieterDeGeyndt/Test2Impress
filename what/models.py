from django.db import models

class What(models.Model):
    whatimage=models.ImageField(verbose_name='What Image', upload_to="whatmedia/whatimage/")
    whattitle = models.CharField(max_length = 200, verbose_name='What Title')
    whatbody=models.TextField(verbose_name='What Body')

    def __str__(self):
        return self.whattitle