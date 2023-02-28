from django import forms
from .models import Lead, User, Agent, Document, Category, UserProfile
from django.contrib.auth.forms import UserCreationForm, UsernameField


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'description',
            'phone_number',
            'email',
            'photo',
            'category',
            'agent',
        )
    
    def __init__(self, *args, **kwargs):
        organisation = kwargs.pop('organisation', None)
        super().__init__(*args, **kwargs)
        
        if organisation:
            categories = Category.objects.filter(organisation=organisation)
            self.fields['category'].queryset = categories
            
            agents = Agent.objects.filter(organisation=organisation)
            self.fields['agent'].queryset = agents


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )


class UploadDocumentModelForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            'lead',
            'title',
            'description',
            'is_secret',
            'file',
            )


class UpdateDocumentModelForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            'lead',
            'title',
            'description',
            'is_secret',
            'file',
            )