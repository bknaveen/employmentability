from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

     # Overriding usercreatiion form to design signup page
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'required': '',
            'name': 'first_name',
            'id': 'inputFirstName',
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'First Name',
            'maxlength': '16',
            'minlength': '6',
        })
        self.fields['last_name'].widget.attrs.update({
            'required': '',
            'name': 'last_name',
            'id': 'inputLastName',
            'type': 'text',
            'class': 'form-control ',
            'placeholder': 'Last Name',
            'maxlength': '16',
            'minlength': '6',
        })
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'inputUsername',
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'johndoe',
            'maxlength': '16',
            'minlength': '6',
        })
        self.fields['email'].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'inputUsername',
            'type': 'email',
            'class': 'form-control ',
            'placeholder': 'example@user.com',
        })
        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-control input-group show_hide_password ',
            'placeholder': '********',
            'maxlength': '22',
            'minlength': '8',
        })
        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class': 'form-control ',
            'placeholder': '********',
            'maxlength': '22',
            'minlength': '8',
        })
        self.fields['role'].widget.attrs.update({
            'required': '',
            'name': 'role',
            'id': 'inputSelectRole',
            'type': 'text',
            'class': 'form-select ',
            'maxlength': '22',
            'minlength': '8',
        })

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2', 'role']
