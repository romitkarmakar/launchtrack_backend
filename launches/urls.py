from django.urls import path

from . import views

urlpatterns = [
    path('getSpaceX', views.getSpaceX, name='getSpaceX'),
    path('getNASA', views.getNASA, name='getNASA'),
    path('getISRO', views.getISRO, name='getISRO'),
    path('getRoscosmos', views.getRoscosmos, name='getRoscosmos'),
    path('getESA', views.getESA, name='getESA'),
    path('getSpaceports', views.getSpacePorts, name='getSpaceports'),
    path('runJobs', views.runJobs, name='runJobs'),
]
