from .forms import UserRegistrationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegistrationForm
    success_url = reverse('homepage')
    template_name = 'registration/registration_form.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


@login_required
def profile_view(request):
    return render(request, 'users/client_profile.html')
