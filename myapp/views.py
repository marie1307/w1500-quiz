from django.shortcuts import render
from .models import Mock_db

# Create your views here.

def main(request):
    employees = Mock_db.objects.all()
    context = {'employees': employees}
    return render(request, 'main.html', context)

def employees(request):
    employees = Mock_db.objects.all()
    context = {'employees': employees}
    return render(request, 'employees.html', context)

def stacks(request):
    stacks = Mock_db.objects.exclude(stack=None).exclude(stack='')
    context = {'stacks': stacks}
    return render(request, 'stacks.html', context)

def team_leads(request):
    team_leads = Mock_db.objects.exclude(team_lead=None).exclude(team_lead='')
    context = {'team_leads': team_leads}
    return render(request, 'team_leads.html', context)

