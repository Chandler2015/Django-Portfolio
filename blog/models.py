from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def summary(self):
        return self.body[:50]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
