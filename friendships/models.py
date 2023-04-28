from django.db import models
from django.conf import settings


class Friendship(models.Model):
    request_from = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='friend_request_from',
                                     on_delete=models.PROTECT)
    request_to = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='friend_request_to',
                                   on_delete=models.PROTECT)
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Friendship'
        verbose_name_plural = 'Friendships'
        db_table = 'friendships'
        unique_together = ('request_from', 'request_to')
