'''
from django.urls import path, reverse_lazy, include
from django.views.generic.edit import CreateView
from .forms import RegistrationForm


urlpatterns = [
    path('auth/registration/', CreateView.as_view(
        template_name='registration/registration_form.html',
        form_class=RegistrationForm,
        success_url=reverse_lazy('blog:index')), name='registration',),
    path('auth/', include('django.contrib.auth.urls')),
]
'''
