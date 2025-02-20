from django.db import models

# Create your models here.
class projects(models.Model):
    title=models.TextField(max_length=20)
    url=models.URLField(default="#",blank=True,null=True)
    def __str__(self):
        return self.title
    
class ticket(models.Model):
    Name=models.TextField(max_length=25)
    email=models.EmailField(max_length=100)
    subject=models.TextField(max_length=25)
    message=models.TextField(max_length=700)
    def __str__(self):
        return self.subject