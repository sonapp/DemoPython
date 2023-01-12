from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name