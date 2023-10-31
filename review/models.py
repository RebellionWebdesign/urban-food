from django.db import models
from django.conf import settings
from user.models import User

class Review(models.Model):
    RATE_CHOICES = (

        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='review_user')
    content = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.author)
