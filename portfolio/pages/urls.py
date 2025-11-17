from django.urls import path
from . import views

urlpatterns=[
    path('',views.resume_view, name='resume'),
    path('about/',views.about_view, name='about')
]