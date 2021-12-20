from django.db import models

class Homepage(models.Model):
    title = models.CharField(verbose_name="Bedrijfsnaam", max_length = 200, default = "Bedrijf")
    logo = models.ImageField(verbose_name="Logo", upload_to="homepagemedia/logo/")
    background = models.ImageField(verbose_name="Achtergrond", upload_to="homepagemedia/background/")
    introtext = models.TextField(verbose_name="Intro")

    def __str__(self):
        return self.title