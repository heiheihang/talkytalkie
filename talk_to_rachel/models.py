import datetime
from django.urls import reverse
from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	post_title = models.TextField()
	post_content = models.TextField(default='I am empty')
	pub_date = models.DateTimeField(null=True)

	def __str__(self):
		return self.post_title

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])