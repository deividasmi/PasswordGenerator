from django import forms
from home.models import  Password, Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class HomeForm(forms.ModelForm):
    post = forms.CharField()
    #widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Write a post...'
#         }
#     ))

    class Meta:
        model = Post
        fields = ('post',)

class ModifyPassword(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = Password
        fields = (
            'website',
            'name',
            'pin'
        )

class CreatePinForm(forms.ModelForm):
    #template_name='/something/else'
    pin = forms.CharField()
    class Meta:
        model = Password
        fields = (
            'website',
            'name',
            'pin'
        )

class PasswordCreationForm(UserCreationForm):
   # website = forms.EmailField(required=True)

    class Meta:
        model = Password
        fields = (
            'website',
            'name',
            'pin',
        )

    def save(self, commit=True):
        new_password = super(PasswordCreationForm, self).save(commit=False)
        new_password.website = self.cleaned_data['website']
        new_password.name = self.cleaned_data['name']
        new_password.pin = self.cleaned_data['pin']

        if commit:
            new_password.save()

        return new_password
