from django import forms
from .models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_name', 'sex', 'age', 'radius', 'gun_control',
                  'abortion', 'immigration', 'drugs', 'healthcare', 'latest')
