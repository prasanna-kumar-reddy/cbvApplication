from django.conf.urls import url
from django.urls import path,include
from cbvApp import views

app_name = 'cbvApp'
urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name = 'detail'),

]
