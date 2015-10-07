from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField()
	tags = TaggableManager() # make instance of TaggableManager

	def __unicode__(self):
		return self.title


class  Thought(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField()
	thought_id = TaggableManager()
	

	def __unicode__(self):
		return self.title
