from django.forms import ModelForm

from .models import Ad


class AdForm(ModelForm):
	class Meta:
		model = Ad
		exclude = ('image_fid',
		           'thumb_fid',
		           'sold',
		           'ad_status',
		           'user_ip',
		           'latitude',
		           'longitude')
