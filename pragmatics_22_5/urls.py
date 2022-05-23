
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
]
