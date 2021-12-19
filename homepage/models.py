from django.db import models

class Homepage(models.Model):
    logo = models.ImageField(name='Homepage Logo', upload_to="homepagemedia/logo/")
    background=models.ImageField(name='Background Image', upload_to="homepagemedia/background/")
    introtext=models.TextField(name='Homepage Intro')