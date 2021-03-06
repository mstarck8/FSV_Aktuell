from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label='Benutzername:')
    password = forms.CharField(max_length=35, label='Password:', widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='Benutzername:')
    password = forms.CharField(max_length=35, label='Password:', widget=forms.PasswordInput)


class ContactForm(forms.Form):
    Name = forms.CharField(max_length=250, required=True)
    Email = forms.EmailField(required=True)
    Nachricht = forms.CharField(required=True, widget=forms.Textarea)
