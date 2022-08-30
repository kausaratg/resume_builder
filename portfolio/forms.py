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
        fields = ("first_name", "last_name", "other_name", "email", "about",
        "phone", "profile_image", "links", "Basic_information", "education", "certificate_and_work_experience", "skills", "hobbies" )
        widgets = {
            'education': SummernoteWidget(attrs={'summernote':{'width':'100%'}} ),
            'certificate_and_work_experience': SummernoteWidget(attrs={'summernote':{'width':'100%'}}),
            'skills': SummernoteWidget(attrs={'summernote':{'width':'100%',}}),
            'hobbies': SummernoteWidget(attrs={'summernote':{'width':'100%'}}),
            'about': SummernoteWidget(attrs={'summernote':{'width':'100%'}}),
            'links': SummernoteWidget(attrs={'summernote':{'width':'100%'}}),
            'Basic_information': SummernoteWidget(attrs={'summernote':{'width':'100%'}}),
        }


