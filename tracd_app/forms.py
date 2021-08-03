from django.forms import ModelForm
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)
from django.http import request
from .models import Book
User = get_user_model()



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):  #used for validation purpose
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password: #un and pwd must be filled
            user = authenticate(username=username, password=password)  #returns a object to user
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')

    password = forms.CharField(widget=forms.PasswordInput)
    Confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'Confirm_password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('Confirm_password')
        if password != password2:
            raise forms.ValidationError("Password must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")


        return super(UserRegisterForm, self).clean(*args, **kwargs)


class Booking_Form(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
    def clean(self, *args, **kwargs):
        return super(Booking_Form, self).clean(*args, **kwargs)