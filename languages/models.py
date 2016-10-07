from __future__ import unicode_literals

from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50,unique=True)
    code = models.CharField(max_length=3, unique=True)
    URL  = models.CharField(max_length=180)

    def __unicode__(self):
        return self.name