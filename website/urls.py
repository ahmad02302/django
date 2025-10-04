from django.urls import path
from website.views import home_view, index_view


urlpatterns=[
    path('home/', home_view, name='home'),
    path('meetings/', index_view, name='meeting')
]