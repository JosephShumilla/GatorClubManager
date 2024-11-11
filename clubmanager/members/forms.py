from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class ClubForm(forms.Form):
    club_name = forms.CharField(max_length=255, label="Club Name")
    club_description = forms.CharField(widget=forms.Textarea, label="Club Description")
    instagram = forms.URLField(required=False, label="Instagram")
    discord = forms.URLField(required=False, label="Discord")
    twitter = forms.URLField(required=False, label="Twitter")