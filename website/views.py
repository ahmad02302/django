from datetime import datetime
from django.shortcuts import render

from meetings.models import Meeting

def home_view(request):
    context={'name':'GLSI',
             'date': datetime.now()}
    return render(request,"home.html", context)

def index_view(request):
    context={'Meetings':Meeting.objects.count()}
    return render(request, "index.html", context)