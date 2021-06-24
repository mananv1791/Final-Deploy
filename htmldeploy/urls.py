import mainpage
import htmldeploy
from django.contrib import admin
from django.urls import path
from django.urls.conf import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainpage.urls')),
]
