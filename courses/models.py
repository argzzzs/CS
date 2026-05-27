from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    units = models.PositiveSmallIntegerField()
    instructor = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f"{self.code} - {self.name}"
