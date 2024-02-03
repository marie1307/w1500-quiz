from django.urls import path, include
from . views import main, employees, stacks, team_leads

urlpatterns = [
    path('main/', main),
    path('employees/', employees),
    path('stacks/', stacks),
    path('team_leads/', team_leads),
]
