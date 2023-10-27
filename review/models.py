from django.db import models
from django.conf import settings 

class Review(models.Model):

    BAD = 0
    MEDIOCRE = 1
    OKAY = 2
    GOOD = 3
    VERY_GOOD = 4

    RATE_CHOICES = (
        (BAD, '1'),
        (MEDIOCRE, '2'),
        (OKAY, '3'),
        (GOOD, '4'),
        (VERY_GOOD, '5'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='review_user')
    content = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.author
