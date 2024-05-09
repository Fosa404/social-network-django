from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import Post, User


class SignupForm(UserCreationForm):
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 2,
        'placeholder': 'Whats on your mind',
    }))

    class Meta:
        model = Post
        fields = ['content']
