from django.db import models

# Create your models here.


class plan(models.Model):
    planname = models.CharField(blank=False, null=False, max_length=50)
    free = models.CharField(blank=False, null=False, max_length=50)
    lite = models.CharField(blank=False, null=False, max_length=50)
    standard = models.CharField(blank=False, null=False, max_length=50)
    plus = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return self.planname
