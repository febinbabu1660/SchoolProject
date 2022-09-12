
from django.urls import path

from Schoolapp import views

urlpatterns = [

    path('',views.index,name='index')

]
