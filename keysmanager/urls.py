from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import (login_view,register_view,logout_view)

urlpatterns = [
	url(r'^login/',login_view, name='login'),
    url(r'^logout/',logout_view, name='logout'),
    url(r'^register/', register_view , name='register'),
    path('admin/', admin.site.urls),
    url(r'^keystate/', include('keystate.urls')),


]
