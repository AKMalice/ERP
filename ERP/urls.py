from django.contrib import admin
from django.urls import include,path
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard/admin',admin_dashboard,name='admin_dashboard'),
]

# Include home module if present
try:
    urlpatterns.append(path('', include('home.urls')))
except:
    pass
