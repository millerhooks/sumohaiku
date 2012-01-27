from django import forms
import datetime
from haiku.models import UserProfile
from django.contrib.auth.models import User

__all__ = ('UserForm', 'UserProfileForm',
           'UserProfileFormA', 'UserProfileFormB')


class UserForm(forms.ModelForm):
    start_stamp = forms.CharField(
        widget=forms.HiddenInput(attrs={'value': datetime.datetime.now()}))

    password = forms.CharField(widget=forms.PasswordInput())
    password_again = forms.CharField(
        widget=forms.PasswordInput(attrs={'title': 'Password Again'}))

    class Meta:
        model = User
        exclude = (
            'is_staff', 'is_active', 'is_superuser',
            'last_login', 'date_joined', 'groups',
            'user_permissions')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class UserProfileFormA(UserProfileForm):
    MOOD_CHOICES = (
        ('0' , 'Happy'),
        ('1' , 'Maudlin'),
        ('2' , 'Languid'),
        ('3' , 'Mercurial'),
    )
    form_version = forms.CharField(
        widget=forms.HiddenInput(attrs={'value' : 'a'}))
    mood = forms.ChoiceField(choices=MOOD_CHOICES)


class UserProfileFormB(UserProfileForm):
    form_version = forms.CharField(
        widget=forms.HiddenInput(attrs={'value' : 'b'}))
