from django import forms
from .models import User, Membership

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

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['club', 'user', 'role']
