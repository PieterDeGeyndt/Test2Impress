from django.db import models

class Who(models.Model):
    whoimage = models.ImageField(name = 'Photo', upload_to="whomedia/whoimage/")
    whofirstname = models.CharField(max_length = 200, name='First Name')
    wholastname = models.CharField(max_length = 200, name='Last Name')
    whodob = models.DateField(name='Date of Birth')
    whobody = models.TextField(name = 'Who am I')
    whocertifications = models.TextField(name = 'Cerftifications')