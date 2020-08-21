from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    important = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name = 'Creation Time')
    is_completed = models.BooleanField(blank=True, null=True)
    time_completed = models.DateTimeField(blank=True, null=True, verbose_name = 'Completion Time')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'ToDo List'
