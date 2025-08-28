# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Appuser(models.Model):

    #__Appuser_FIELDS__
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    emai = models.CharField(max_length=255, null=True, blank=True)

    #__Appuser_FIELDS__END

    class Meta:
        verbose_name        = _("Appuser")
        verbose_name_plural = _("Appuser")


class Plugin(models.Model):

    #__Plugin_FIELDS__
    slug = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField()
    is_premium = models.BooleanField()
    version = models.CharField(max_length=255, null=True, blank=True)

    #__Plugin_FIELDS__END

    class Meta:
        verbose_name        = _("Plugin")
        verbose_name_plural = _("Plugin")



#__MODELS__END
