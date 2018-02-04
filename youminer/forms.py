from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import Comment

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
    	model = User
    	fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Pseudo"
        self.fields['email'].label = "Email"
        self.fields['password'].label = "Mot de passe"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""
