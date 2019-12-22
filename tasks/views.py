from django.shortcuts import render


def welcome(request):
    """Return the base.html file"""
    return render(request, 'base.html')
