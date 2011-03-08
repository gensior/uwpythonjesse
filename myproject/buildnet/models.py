from django.db import models
import random, string

class Station(models.Model):
	name = models.CharField(max_length=255, unique=True)
	
	def __unicode__(self):
		return self.name

class Part(models.Model):
	word = models.CharField(max_length=100, unique=True)
	
	def __unicode__(self):
		return self.word

class Installation(models.Model):
	part = models.ForeignKey('Part')
	station = models.ForeignKey('Station')
	order = models.IntegerField(blank=True)
	qrcode = models.CharField(max_length=100, unique=True, editable=False, )
	installed = models.BooleanField(default=False)
	
	def save(self, force_insert=False, force_update=False):
		try:
			recent = Installation.objects.filter(station=self.station).order_by('-order')[0]
			self.order = recent.order + 1
		except IndexError:
			self.order = 1
		self.qrcode = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
		super(Installation, self).save(force_insert, force_update)
	
	def __unicode__(self):
			return self.qrcode