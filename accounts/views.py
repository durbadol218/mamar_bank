from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'userRegistration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form) #automatically call korar jonno ai line lekhlam...jodi sobthik thaake tobe automatically kaaj korbe!
    

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    
# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('homepage')
class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('homepage')