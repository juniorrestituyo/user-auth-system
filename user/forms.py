from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].widget.attrs.update({'class': 'input100', 'placeholder': 'Name'})
        self.fields["email"].widget.attrs.update({'class': 'input100', 'placeholder': 'Email'})
        self.fields["username"].widget.attrs.update({'class': 'input100', 'placeholder': 'Username'})
        self.fields["password1"].widget.attrs.update({'class': 'input100', 'placeholder': 'Password'})
        self.fields["password2"].widget.attrs.update({'class': 'input100', 'placeholder': 'Confirm Password'})

