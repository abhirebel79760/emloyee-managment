from django.db import models


# Create your models here.


class Reply(models.Model):
    user_name = models.CharField(max_length=200)

    remark = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name
