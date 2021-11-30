from django.db import models

class FeedbackData(models.Model):
    Name=models.CharField(max_length=20)
    Rating=models.IntegerField()
    Date=models.DateField(auto_now_add=True)
    Location=models.CharField(max_length=20)
    Feedback=models.TextField(max_length=100)


