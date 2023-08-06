from django.urls import path
from .views import profile_view, RegistrationView

app_name = 'users'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('signup/', RegistrationView.as_view(), name='signup'),
]
