from django.db import models

class Homepage(models.Model):
    title = models.CharField(name = 'Name Company', max_length = 200, default = "")
    logo = models.ImageField(name ='Homepage Logo', upload_to="homepagemedia/logo/")
    background=models.ImageField(name='Background Image', upload_to="homepagemedia/background/")
    introtext=models.TextField(name='Homepage Intro')

    def __str__(self):
        return self.title