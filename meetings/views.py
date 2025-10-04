from django.shortcuts import get_object_or_404, render

from .models import Meeting

def Meetings_List(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings.html',{'meetings': meetings})

def detail(request, id):
    meeting = Meeting.objects.get(id=id)
    return render(request, 'detail.html',{'m': meeting})