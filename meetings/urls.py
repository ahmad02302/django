from django.urls import  path
from meetings.views import Meetings_List, detail


urlpatterns=[
    path('all/', Meetings_List, name='list'),
    path('detail/<int:id>/', detail, name='details')
    ]