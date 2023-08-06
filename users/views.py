from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .forms import UserRegistrationForm
from django.urls import reverse_lazy


@login_required
def profile_view(request):
    return render(request, 'users/client_profile.html')


class RegistrationView(FormView):
    """
    Регистрация пользователя.
    """
    form_class = UserRegistrationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('homepage:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
