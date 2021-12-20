from django.db import models

class Who(models.Model):
    whoimage = models.ImageField(verbose_name = 'Photo', upload_to="whomedia/whoimage/")
    whofirstname = models.CharField(max_length = 200, verbose_name='First Name')
    wholastname = models.CharField(max_length = 200, verbose_name='Last Name')
    whodob = models.DateField(verbose_name='Date of Birth')
    whobody = models.TextField(verbose_name = 'Who am I')
    whocertifications = models.TextField(verbose_name = 'Cerftifications')

    def __str__(self):
        return self.whofirstname