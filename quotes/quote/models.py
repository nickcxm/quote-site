from django.db import models

# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Quote(models.Model):
    text=models.TextField()
    author=models.CharField(max_length=20)
    created_time=models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering=['-created_time']
