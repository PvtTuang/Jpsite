from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="Your password must contain at least 8 characters."
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)