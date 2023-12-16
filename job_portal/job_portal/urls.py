"""
URL configuration for job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from job.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'job'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ,name="index"),
    path('admin_login',admin_login,name="admin_login"),
    path('user_login',user_login,name="user_login"),
    path('recruiter_login',recruiter_login,name='recruiter_login'),
    path('user_signup',user_signup,name='user_signup'),
    path('user_home',user_home,name='user_home'),

]

# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns()
