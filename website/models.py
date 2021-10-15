from django.db import models

# Create your models here.
class Sentiment(models.Model):
    input=models.CharField(max_length=100)
    pos=models.FloatField(default=0)
    neg = models.FloatField(default=0)
    neu = models.FloatField(default=0)


