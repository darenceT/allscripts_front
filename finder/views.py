from django.shortcuts import render
from .models import Data

def index(request):
    data = Data.objects.all()
    context = {
        'data': data
    }
    return render(request, 'finder/index.html', context)

def profile(request, profile_id):
    profile = Data.objects.get(pk=profile_id)
    similar = Data.objects.filter(
        specialty__icontains=profile.specialty
    ).exclude(
        name__icontains=profile.name
    )
    context = {
        'profile': profile,
        'similar': similar,
    }
    return render(request, 'finder/profile.html', context)