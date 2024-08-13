from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from accounts.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control my-2'})
        self.fields['password'].widget.attrs.update({'class': 'form-control my-2'})


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'gender', 'birthday', 'username', 'password1', 'password2')

    help_texts = {
        'username': None,
        'password1': None,
        'password2': None,
    }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control my-2'})
            if self.errors.get(field_name):
                field.widget.attrs.update({'class': 'form-control my-2 is-invalid'})

        self.fields['birthday'].widget = forms.DateInput(attrs={"type": "date", 'class': "form-control mb-2"})
