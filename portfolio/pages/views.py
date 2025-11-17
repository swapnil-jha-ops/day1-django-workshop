from django.shortcuts import render

# Create your views here.

def resume_view(request):
    return render(request,"resume.html")

def about_view(request):
    return render(request,"about.html")

