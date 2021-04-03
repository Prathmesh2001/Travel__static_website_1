from django.shortcuts import render

# Create your views here.

def contact_page(request):
    return render(request, "s1_contact.html")

def home_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "s1_about.html")