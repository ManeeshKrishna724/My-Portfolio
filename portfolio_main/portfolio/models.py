from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    demo = models.FileField(upload_to="demos")
    description = models.TextField()
    project_url = models.URLField(blank=True)
    created_date = models.DateField()
    thumbnail = models.ImageField(upload_to="thumbnails")

    def __str__(self) :
        return self.name