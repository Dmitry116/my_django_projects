from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Profile

class AboutUserView(TemplateView):
    template_name = 'myauth/about_user.html'


class RegisterView(CreateView):
    form_class = UserCreationForm  # валидация данных. проверка что первый и второй пароль введен верно
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about_user')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response
