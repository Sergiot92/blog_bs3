from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=300)
	content = models.TextField()
	creation_date = models.DateTimeField(auto_now_add=True)    
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	user = models.ForeignKey(User)
	content = models.TextField()
	creation_date = models.DateTimeField(auto_now_add=True) 
	def __unicode__(self):
		return self.content

class Post_Comment(models.Model):
	post = models.ForeignKey(Post)
	comment = models.ForeignKey(Comment)
