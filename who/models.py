from django.db import models
from django.utils import timezone

class Who(models.Model):
    whoimage = models.ImageField(verbose_name = 'Photo', upload_to="whomedia/whoimage/",default="")
    whofirstname = models.CharField(max_length = 200, verbose_name='First Name',default="")
    wholastname = models.CharField(max_length = 200, verbose_name='Last Name',default="")
    whodob = models.DateField(verbose_name='Date of Birth',default=timezone.now)
    whobody = models.TextField(verbose_name = 'Who am I',default="")
    whocertifications = models.TextField(verbose_name = 'Cerftifications',default="")
    whoemail = models.CharField(max_length = 200, verbose_name = 'e-mailaddress', default ="")
    whoaddress = models.TextField(verbose_name='Address', default="")
    whophone = models.CharField(max_length = 200, verbose_name='Tel nr', default="+32 (0) ")
    whocv = models.FileField(verbose_name="Curriculum Vitae", upload_to="whomedia/wocv/",default="")

    def __str__(self):
        return self.whofirstname