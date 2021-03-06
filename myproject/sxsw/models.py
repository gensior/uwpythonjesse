from django.db import models
import datetime
from django.contrib.auth.models import User


class Party(models.Model):
	name = models.CharField(max_length=255)
	starttime = models.DateTimeField('Start Time')
	endtime = models.DateTimeField('End Time', null=True)
	location = models.CharField(max_length=100)
	drinks = models.BooleanField(default=False)
	food = models.BooleanField(default=False)
	website = models.URLField(verify_exists=True)
	attendees = models.ManyToManyField(User)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		ordering = ['starttime']
		verbose_name_plural = 'Parties'
	
                  