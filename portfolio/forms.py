from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from portfolio.models import Portfolio
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ("first_name", "last_name", "other_name", "email",
        "phone", "education", "certificate", "skills", "hobbies")
        widgets = {
            'education': SummernoteWidget(attrs={'width':'100%', 'summernote': {'background':'rgba(255,255,255,0.1', 'color':'rgba(255,255,255,0.1'}}),
            'certificate': SummernoteWidget(),
            'skills': SummernoteWidget(),
            'hobbies': SummernoteWidget()
        }


