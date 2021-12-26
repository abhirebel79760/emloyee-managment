from django.db import models

# Create your models here.


class Employe(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=50)
    epm_deparment = models.CharField(max_length=100)

    def __str__(self):
        return self.emp_name
