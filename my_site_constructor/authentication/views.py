from django.contrib.auth import views
from django.views import generic

from authentication import forms
from my_site_constructor import settings


class LoginView(views.LoginView):
    form = forms.LoginForm
    redirect_authenticated_user = settings.LOGIN_REDIRECT_URL
    template_name = 'login.html'


class LogoutView(views.LogoutView):
    redirect_field_name = settings.LOGOUT_REDIRECT_URL


class RegisterFormView(generic.FormView):
    form_class = forms.RegisterForm
    success_url = '/login/'
    template_name = 'registration.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)