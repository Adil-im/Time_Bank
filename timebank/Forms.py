from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Post

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'auth-input'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'auth-input'})
        self.fields['password1'].widget.attrs.update({'class': 'auth-input'})
        self.fields['password2'].widget.attrs.update({'class': 'auth-input'})

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'auth-input'})
        self.fields['password'].widget.attrs.update({'class': 'auth-input'})

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'topic', 'hours_offered']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'post-input', 'placeholder': 'Post Title'}),
            'description': forms.Textarea(attrs={'class': 'post-textarea', 'placeholder': 'Describe your time bank offer or request'}),
            'topic': forms.Select(attrs={'class': 'post-select'}),
            'hours_offered': forms.NumberInput(attrs={'class': 'post-input', 'min': '0.5', 'max': '10', 'step': '0.5'})
        }
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
        
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 20:
            raise forms.ValidationError("Description must be at least 20 characters long.")
        return description