from django.urls import path
from .views import homepagesview

urlpatterns =[
    path('', homepagesview, name='home'),

]