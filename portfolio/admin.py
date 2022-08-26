from django.contrib import admin
from portfolio.models import Portfolio
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('education', 'certificate', 'skills', 'hobbies')

admin.site.register(Portfolio, PostAdmin)
