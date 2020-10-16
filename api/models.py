from django.db import models

# Create your models here.


class userInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    weight = models.IntegerField()
    height = models.IntegerField()
    fitnessGoals = models.CharField(max_length=30)

    def __str__(self):
        return self.name
