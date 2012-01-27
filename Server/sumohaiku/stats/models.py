from django.db import models
from django.contrib.auth.models import User

STAT_TYPE_CHOICES = (
    ('0' , 'Form'),
    ('1' , 'Navigation'),
    ('2' , 'Interactive'),
)


class Asset(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=STAT_TYPE_CHOICES)

    def __unicode__(self):
        return self.name


class Stat(models.Model):
    asset = models.ForeignKey(Asset)
    user = models.ForeignKey(User, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    start_stamp = models.DateTimeField()
    end_stamp = models.DateTimeField()

    def __unicode__(self):
        return self.asset.name
