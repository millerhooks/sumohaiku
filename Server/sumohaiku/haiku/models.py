from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField


USER_TYPE_CHOICES = (
    ('0' , 'Blacksmith'),
    ('1' , 'Wizard'),
    ('2' , 'Bard'),
    ('3' , 'Cleric'),
)

class UserProfile(models.Model):
    """
    Extended user profile module

    """
    user = models.ForeignKey(User, blank=True, null=True)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = USStateField()
    zip_code = models.IntegerField()

    phone_home = PhoneNumberField(blank=True)
    phone_cell = PhoneNumberField(blank=True)
    phone_fax = PhoneNumberField(blank=True)

    type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)

    def __unicode__(self):
        return self.user.username

class Haiku(models.Model):
    """
    Haikus from the interwebs.

    """
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __unicode__(self):
        return self.name
