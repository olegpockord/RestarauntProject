from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import auth, messages
from django.views.generic import CreateView

from user.forms import UserLoginForm, UserRegistrationForm

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    # success_url = reverse_lazy('main:index')

    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('users:login'):
            return redirect_page
        return reverse_lazy('main:index')

    def form_valid(self, form):
        user = form.get_user()

        if user:
            auth.login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
           
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context


class RegistrationView(CreateView):
    template_name = 'user/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context
    
    def form_valid(self, form):
        
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)
        
            return HttpResponseRedirect(self.success_url)
    

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))



# def UserAuth(request):
    
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username = username, password = password)
#             if user:
#                 auth.login(request, user)
#                 messages.success(request, f"{username}, Вы вошли в аккаунт")


#                 return HttpResponseRedirect(reverse('main:index'))
            
#     else:
#         form = UserLoginForm()

#     contex = {
#         'title': 'Авторизация',
#         'form': form,
#     }

#     return render(request, 'user/login.html', contex)


# def CreateAcc(request):


#     if request.method == 'POST':

#         form = UserRegistrationForm(data = request.POST)
#         if form.is_valid():
#             form.save()
            
#             user = form.instance
#             auth.login(request, user)

#             messages.success(request, f"{user.username}, Вы зарегистрировались")
#             return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserRegistrationForm()

#     contex = {
#         'title': 'Регистрация',
#         'form': form,
#     }

#     return render(request, 'user/registration.html', contex)

