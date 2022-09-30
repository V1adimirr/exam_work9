from django import forms

from webapp.models import ImagesModel, AlbumModel


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImagesModel
        fields = ['photo', 'signature', 'album']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = ['image_name', 'description']


