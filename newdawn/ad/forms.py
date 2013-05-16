from django.forms import ModelForm

from .models import Ad


class AdForm(ModelForm):
	class Meta:
		model = Ad
		fields = ('subject', 'body', 'category', 'price', 'user_phone', 'user_email')
