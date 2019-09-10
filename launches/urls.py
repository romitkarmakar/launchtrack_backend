from django.urls import path

from . import views

urlpatterns = [
    path('get/<str:name>/', views.getLaunches, name='getLaunches'),
    path('getSpaceports', views.getSpacePorts, name='getSpaceports'),
    path('runJobs', views.runJobs, name='runJobs'),
    path('getCompanies', views.getCompanies, name='getCompanies'),
]
