from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    review_score = models.FloatField(default=0)
    years = models.CharField(max_length=100, default=0)

    phone = models.CharField(default=False, max_length=100)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name