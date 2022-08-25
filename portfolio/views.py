from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
import portfolio
from portfolio.forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
class Home(TemplateView):
    template_name = 'portfolio/index.html'


###############################      REGISTER    #################################
def signup_user(request):
    form_name = UserForm()
    if request.method =='POST' :
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
                return redirect('index')
            else:
                return redirect('signin_user')
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'portfolio/signin.html', context)
    
        

