from django.urls import path

from accountapp.views import hello_world

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world')
]


#127.0.0.1.:8000/accoiunt/hello_world