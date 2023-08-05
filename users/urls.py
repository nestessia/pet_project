from django.urls import path
from django.views.generic.edit import CreateView
from users.forms import UserRegistrationForm
from .views import profile_view

app_name = 'users'

urlpatterns = [
    path('signup/', CreateView.as_view(
         template_name='registration/registration_form.html',
         form_class=UserRegistrationForm)),
    path('profile/', profile_view, name='profile'),
]
