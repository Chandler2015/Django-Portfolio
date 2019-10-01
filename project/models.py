from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    summary = models.CharField(max_length=200, null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    pub_date = models.DateField(null=True, blank=True)
