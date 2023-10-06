from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
from app.forms import *
# Create your views here.

# Normal html page rendering
class TempViews(TemplateView):
    template_name = 'TempViews.html'


# sending context by using templaeview class
class Temp_context(TemplateView):
    template_name='Temp_context.html'

    def get_context_data(self,**kwargs):
        EDCO = super().get_context_data(**kwargs)
        EDCO['name']='Satish kumar'
        return EDCO
    
# sending form by using templaeview class
class Temp_form(TemplateView):
    template_name='Temp_form.html'

    def get_context_data(self,**kwargs):
        EDCO = super().get_context_data(**kwargs)
        EDCO['SFO']=StudentForm()
        return EDCO

    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('<center><h1 style="color: green;">Data inserted successfully</h1></center>')

