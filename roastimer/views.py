from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(
        request, 
        'index.html',
        {
            'title': 'Coffee roast timer - Log your home roasts'
        } 
    )

def about(request):
    return render(
        request,
        'about.html',
        {
            'title': 'Coffee roast timer - About the site'
        }
    )