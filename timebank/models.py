from django.db import models

# Create your models here.
class Post(models.Model):
    TOPIC_CHOICES = [
        ('catering', 'Catering'),
        ('educational', 'Education'),
        ('cleaning', 'Cleaning'),
        ('tech', 'Tech'),
        ('recreational', 'Recreational'),
        ('outdoor', 'Outdoor')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    hours_offered = models.DecimalField(max_digits=4, decimal_places=1, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title