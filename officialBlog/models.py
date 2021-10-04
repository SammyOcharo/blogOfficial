from django.db import models

# Create your models here.

class Blogs(models.Model):
    Title = models.CharField(max_length=100)
    Scriptures = models.CharField(max_length=255)
    Message = models.TextField()
    Time_Entry = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title