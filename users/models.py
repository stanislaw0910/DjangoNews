from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    verification = models.BooleanField(default=False)
    news_count = models.IntegerField(verbose_name='количество опубликованных новостей', default=0)

    class Meta:
        permissions = (
            ('can_verificate', 'Может верифицировать'),
        )

    def __str__(self):
        return self.user.username
