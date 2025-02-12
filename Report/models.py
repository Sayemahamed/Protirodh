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


class CrimeReport(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crime_images/', blank=True, null=True)
    video = models.FileField(upload_to='crime_videos/', blank=True, null=True)
    post_time = models.DateTimeField(auto_now_add=True)
    crime_time = models.DateTimeField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ai_description_generated = models.BooleanField(default=False)

    @property
    def vote_score(self):
        return self.votes.aggregate(total=models.Sum('vote'))['total'] or 0

    def get_share_link(self):
        """Returns the full URL to share this post."""
        return f"/reports/detail/{self.id}/"

    def __str__(self):
        return self.title

class Comment(models.Model):
    crime_report = models.ForeignKey(CrimeReport, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    proof_image = models.ImageField(upload_to='comment_proofs/', blank=True, null=True)
    proof_video = models.FileField(upload_to='comment_proof_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)  # Allow comment replies

    def __str__(self):
        return f"Comment by {self.user.username} on {self.crime_report.title}"

class Vote(models.Model):
    VOTE_CHOICES = (
        (1, 'Upvote'),
        (-1, 'Downvote'),
    )
    crime_report = models.ForeignKey(CrimeReport, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('crime_report', 'user')  # Ensure one vote per user per report

    def __str__(self):
        return f"{self.user.username} voted {self.vote} on {self.crime_report.title}"

# class Notification(models.Model):
#     recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
#     sender = models.ForeignKey(User, on_delete=models.CASCADE)
#     crime_report = models.ForeignKey(CrimeReport, on_delete=models.CASCADE, null=True, blank=True)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
#     vote = models.ForeignKey(Vote, on_delete=models.CASCADE, null=True, blank=True)
#     message = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Notification for {self.recipient.username} - {self.message}"