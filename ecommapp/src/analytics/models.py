from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .util import get_client_ip
from .signals import object_viewed_signal

User = settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #Can be any model
    object_id = models.PositiveIntegerField() #Can be Id of the respective model
    content_object = GenericForeignKey('content_type', 'object_id') #Gives out instance
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed as %s" %(self.content_object, self.timestamp)

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'