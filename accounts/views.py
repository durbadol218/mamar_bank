from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm, UserUpdateForm
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
    

class UserUpdateView(View):
    template_name = 'profile.html'
    
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form}) #automatically call korar jonno ai line lekhlam...jodi sobthik thaake tobe automatically kaaj korbe!
    
