from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class SignUpForm(UserCreationForm, forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30, required=True)
    email = forms.EmailField(label='Email', max_length=254, required=True)
    password1 = forms.CharField(label='Password', max_length=30, required=True)
    password2 = forms.CharField(label='Password confirmation', max_length=30, required=True)
    phone_number = forms.CharField(label='Phone', max_length=30, required=True)
    country = forms.CharField(label='Country', max_length=30, required=True)
    first_name = forms.CharField(label='Username', max_length=30, required=True)
    last_name = forms.CharField(label='Username', max_length=30, required=True)

    class Meta:
        model = User
        fields = (
            'profile_image', 'username', 'email', 'password1', 'password2',
            'country', 'phone_number', 'first_name', 'last_name')
        extra_kwargs = {'password1': {'write_only': True},
                        'password2': {'write_only': True}, 'email': {'unique': True}}
