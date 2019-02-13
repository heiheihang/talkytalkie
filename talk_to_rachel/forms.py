import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from django.utils import timezone

from .models import Post
from django.contrib.auth.models import User

class PublishPost(forms.Form):
	post_title = forms.CharField(widget=forms.Textarea)
	post_content = forms.CharField(widget=forms.Textarea)
	pub_date = timezone.now()


class TestForm(ModelForm):
	class Meta:
		model = Post 
		fields = ['post_title', 'post_content', 'pub_date']