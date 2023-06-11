from django.db import models

# Create your models here.
class Project(models.Model):
    class Meta:
        ordering = ["order_number"]

    name = models.CharField(max_length=200)
    demo = models.FileField(upload_to="demos")
    order_number = models.IntegerField(null=True)
    description = models.TextField()
    project_url = models.URLField(blank=True)
    created_date = models.DateField()
    thumbnail = models.ImageField(upload_to="thumbnails")

    def __str__(self) :
        return self.name