from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView,  UpdateView
from portfolio.forms import UserForm, PortfolioForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from portfolio.models import Portfolio
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(TemplateView):
    template_name = 'portfolio/index.html'

class personal_info(LoginRequiredMixin, CreateView):
    login_url = '/signin/'
    form_class = PortfolioForm
    model = Portfolio
    context_name = "form"
    template_name = 'portfolio/personal_info.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.username = self.request.user
        obj.save()
        return redirect('index')

class UpdatePersonal_info(LoginRequiredMixin, UpdateView):
    login_url = '/signin/'
    form_class = PortfolioForm
    model = Portfolio
    context_name = "form"
    template_name = 'portfolio/personal_info.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.username = self.request.user
        obj.save()
        return redirect('index')


###############################      REGISTER    #################################
def signup_user(request):
    form_name = UserForm()
    if request.method =="POST":
        form_name = UserForm(request.POST)
        if form_name.is_valid():
            form_name.save()
            messages.success(request, "You have registered successfully")
            return redirect('signin')
        else:
            messages.error(request, 'Invalid input') 
            return redirect('signup')
    else:
        messages.error(request, 'Invalid input')
        context = {'form_name':form_name}
        return render(request, 'portfolio/signup.html', context)

def signin_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('personal_info')
            else:
                messages.error('Invalid input.. Please try again.')
                return redirect('signin_user')
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'portfolio/signin.html', context)

def logout_user(request):
    logout(request)
    return redirect('signin')
    
        

