from django.db import models

# Create your models here.
#a model that takes day, task title , description and date

class TaskModel(models.Model):
    DAY_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    duration = models.CharField()


    def __str__(self):
        return f"{self.title} on {self.day} ({self.date})"