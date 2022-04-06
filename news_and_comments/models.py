from django.db import models
from django.conf import settings


class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.title} {self.created.strftime("%Y:%M:%d")}{self.active}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name_plural = 'News'
        permissions = (
            ('can_publicate', 'Может опубликовать'),
        )


class Tags(models.Model):
    name = models.CharField(max_length=20)
    news = models.ManyToManyField(News)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Comments(models.Model):
    username = models.CharField(max_length=10)
    text = models.CharField(max_length=100)
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        text_gt_15 = len(self.text)>15
        return f'{self.username}: {self.text[:15]}...' if text_gt_15 else f'{self.username}: {self.text[:15]}'

    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = 'Comment'

