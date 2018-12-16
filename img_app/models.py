from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    upload = models.ImageField(upload_to='%Y/%m/%d', null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title