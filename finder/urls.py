from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:profile_id>/', views.profile, name='profile'),
]