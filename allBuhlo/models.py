from django.db import models
from django.utils import timezone

class Alcohol(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.TextField()
	content = models.TextField()
	image = models.ImageField()
	publish_date = models.DateTimeField(default=timezone.now)
	ingredients = models.ManyToManyField('IngLitr')

	def titleReplacing(self):
		return self.title.replace(' ','_')

	def __str__(self):
		return self.title

	def somesave(self):
		self.save()

class Ingridient(models.Model):
	name = models.TextField()
	
	def __str__(self):
		return self.name

class IngLitr(models.Model):
	litr = models.TextField()
	ingname = models.ForeignKey('Ingridient')

	def __str__(self):
		return self.litr +" "+ str(self.ingname.name)