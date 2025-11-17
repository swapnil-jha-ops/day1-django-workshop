"""
URL configuration for students project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.display_landing,name='home'),
    path('addstudent/',view.add_student,name='Astudent'), 
    path('addproff/',view.add_proff,name='Aproff'), 
    path('addfacility/',view.add_facility,name='Afacility'),
    path('viewstudent/',view.view_student,name='Vstudent'), 
    path('viewproff/',view.view_proff,name='Vproff'), 
    path('viewfacility/',view.view_facility,name='Vfacility'),
    path('chatbot/', view.chatbot, name='chatbot'),
    path('chatbot/view',view.render_chatbot, name='chatbot_view') 

]
