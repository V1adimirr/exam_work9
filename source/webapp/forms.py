from django import forms

from webapp.models import ImagesModel


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImagesModel
        fields = ['photo', 'signature', 'album']

