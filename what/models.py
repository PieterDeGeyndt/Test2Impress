from django.db import models

class What(models.Model):
    whatimage=models.ImageField(name='What Image', upload_to="whatmedia/whatimage/")
    whattitle = models.CharField(max_length = 200, name='What Title')
    whatbody=models.TextField(name='What Body')

    def __str__(self):
        return self.whattitle