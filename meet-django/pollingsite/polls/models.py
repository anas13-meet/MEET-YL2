from django.db import models

class Polls(models.Model):
	
	question = models.CharField(max_length = 200)

class answer(models.Model):

	Answer = models.CharField(max_length=50)
	Votes = models.integerField (default=0)
	poll = models.ForeignKey(Poll)