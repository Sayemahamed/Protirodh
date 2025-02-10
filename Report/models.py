from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Report(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='crime-images/', null=True, blank=True)
    video = models.FileField(upload_to='crime-videos/', null=True, blank=True)
    report_time = models.DateTimeField(auto_now_add=True)
    crime_time = models.DateTimeField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    comment = models.TextField()
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comment-images/', null=True, blank=True)
    video = models.FileField(upload_to='comment-videos/', null=True, blank=True)
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.report.title} - {self.commented_by.username}'
