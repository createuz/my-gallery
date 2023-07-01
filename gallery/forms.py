from django import forms
from gallery.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'title')
        labels = {'image': "", 'user': ""}
        extra_kwargs = {'user': {'required': False}}

    image = forms.ImageField(label='Select a file')

    title = forms.CharField(label='Title')
