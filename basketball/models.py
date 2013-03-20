from django.db import models

# Create your models here.
class Player(models.Model):
	name = models.CharField(unique=False, max_length=25)
	number = models.CharField(unique=True, max_length=3)
	position = models.CharField(unique=False, max_length=25)
	height = models.IntegerField(unique=False, max_length=5)
	weight = models.IntegerField(unique=False, max_length=5)
	year = models.CharField(unique=False, max_length=20)
	hometown = models.CharField(unique=False, max_length=50)
	high_school = models.CharField(unique=False, max_length=50)
	major = models.CharField(unique=False, max_length=50)
	img = models.CharField(max_length =100)
	bio = models.CharField(max_length=5000)

	def __unicode__(self):
		return U'%s %s' %(self.name, self.number)

class Team(models.Model):
	name = models.CharField(unique=False, max_length=50)
	season = models.CharField(unique=False, max_length=12)
	acc_record = models.CharField(unique=False, max_length=10)
	overall_record = models.CharField(unique=False, max_length=10)
	ranking = models.CharField(unique=False, max_length=3)
	players = models.ManyToManyField(Player)

	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super(Team, self).save(*args, **kwargs)

	def __unicode__(self):
		return U'%s %s %s %s' %(self.name, self.ranking, self.season, self.overall_record)