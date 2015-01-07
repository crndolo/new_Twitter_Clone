from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
	author 			= models.ForeignKey(User)
	message 		= models.CharField(max_length = 160)
	date_created 	= models.DateTimeField(auto_now = True)
	slug 			= models.SlugField(max_length = 50)

	def __unicode__(self):
		return unicode(self.message)

class Retweet(models.Model):
	retweeted_message 	= models.ForeignKey(Tweet)
	retweeter 			= models.ForeignKey(User)
	date_retweeted 		= models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return unicode(self.retweeter)

class Reply(models.Model):
	replier 			= models.ForeignKey(User)
	message 			= models.ForeignKey(Tweet)
	replied_message 	= models.CharField(max_length = 160)
	reply_date 			= models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return unicode(self.replier)
