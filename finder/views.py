from django.shortcuts import render
from .models import Data

def index(request):
    """
    Gives list of doctors in home page
    param request: use loads home page or click return to home page
    return: execution of main page
    """
    data = Data.objects.all()
    context = {
        'data': data
    }
    return render(request, 'finder/index.html', context)

def profile(request, profile_id):
    """
    Display profile of interested doctor. 
    Display similar doctors by speciality, exlude interested doctor, and
    order by preferring doctor with highest review score
    param request: when user clicks on a specific doctor in home page
    param profile_id: the selected doctor, a Data object
    return: execution of profile page
    """
    profile = Data.objects.get(pk=profile_id)
    similar = Data.objects.filter(
        specialty__icontains=profile.specialty
    ).exclude(
        name__icontains=profile.name
    ).order_by(
        "-review_score" 
    )
    context = {
        'profile': profile,
        'similar': similar,
    }
    return render(request, 'finder/profile.html', context)