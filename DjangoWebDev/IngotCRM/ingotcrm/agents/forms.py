from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from leads.models import Agent, User

USER = get_user_model()


class AgentCreateModelForm(forms.ModelForm):
    class Meta:
        model = USER
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'position',
            'photo',
        )


class AgentUpdateModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'position',
        )


class AgentProfileUpdateModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'photo',
        )