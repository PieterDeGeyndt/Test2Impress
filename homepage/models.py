from django.db import models

class Homepage(models.Model):
    title = models.CharField(verbose_name="Bedrijfsnaam", max_length = 200, default = "")
    logo = models.ImageField(verbose_name="Logo", upload_to="homepagemedia/logo/", default="")
    background = models.ImageField(verbose_name="Achtergrond", upload_to="homepagemedia/background/", default="")
    introtext = models.TextField(verbose_name="Intro",default="")

    def __str__(self):
        return self.title