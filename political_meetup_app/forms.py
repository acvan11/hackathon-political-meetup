from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_name', 'sex', 'age', 'radius', 'gun_control',
                  'abortion', 'immigration', 'drugs', 'healthcare', 'latest')
