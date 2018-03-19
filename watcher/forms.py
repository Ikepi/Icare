from django import forms


class SignInForm(forms.Form):
    InputUserName = forms.CharField(max_length=10)
    InputPassword = forms.CharField(min_length=8, max_length=20)


class SignUpForm(forms.Form):
    InputUserName = forms.CharField(max_length=10)
    InputPassword = forms.CharField(min_length=8, max_length=20)
    InputConfirmPassword = forms.CharField(min_length=8, max_length=20)
    InputEmail = forms.EmailField()
