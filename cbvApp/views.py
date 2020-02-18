from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    #   school_list will be converted to school_list like that automatically at cbvbase html page
    #or else u can define the abv cntxt obj nme
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbvApp/school_detail.html'  #converted to school thats it bcz its detail view

#class IndexView(TemplateView):
#    template_name = 'index.html'
#
#    def get_context_data(self **kwargs):
#        context = super().get_context_data(self,**kwargs)
#        context['injectme'] = 'BasicInjection'
#        return context
