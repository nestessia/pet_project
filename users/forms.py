from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    """
    Переопределенная форма регистрации пользователей
    """
    username = forms.CharField(label="Имя пользователя", max_length=65)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name',
                                                 'last_name')

    def clean_email(self):
        """
        Проверка email на уникальность
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(
                                            username=username).exists():
            raise forms.ValidationError(
                'Такой email уже используется в системе')
        return email
