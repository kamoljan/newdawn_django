from django.forms import ModelForm
from django.forms.widgets import HiddenInput, FileInput

from .models import Ad


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ('subject', 'body', 'category', 'price', 'user_phone', 'user_name', 'user_email',
                  'latitude', 'longitude', 'image_fid')
        widgets = {'latitude': HiddenInput(), 'longitude': HiddenInput(), 'image_fid': FileInput(),
                   'user_name': HiddenInput(), 'user_email': HiddenInput()}

    def __setattr__(self, name, value):
        return super(AdForm, self).__setattr__(name, value)

