from django.db import models
from datetime import datetime


# Create your models here.

status_CHOICES = (
    ('pending', 'PENDING'),
    ('completed', 'COMPLETED'),
    ('inprocess', 'INPROCESS'),
)


def get_today():
    return datetime.now()


TODAY = get_today

DATE_SELECTION = (
    (TODAY, TODAY),

)


class Purchasetask(models. Model):
    first_name = models.CharField(max_length=50)
    discription = models.CharField(max_length=200)
    deaprtment = models.CharField(max_length=225)
    created_by = models.CharField(max_length=50)
    submision_date = models.CharField(max_length=250, default="NOT CHECKED")
    ramark = models.CharField(max_length=100)
    repoting_data = models.CharField(max_length=50, default="datetime.now")
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=300, choices=status_CHOICES, default="pending")
    checked = models.BooleanField(max_length=225, default=False)

    def __str__(self):
        return self.created_by
