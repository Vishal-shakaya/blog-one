from post import models
from django import forms
class PostForm(forms.ModelForm):
	class Meta:
		model = models.post
		fields=['title' , 'content','image']
