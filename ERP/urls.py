from django.contrib import admin
from django.urls import include,path
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard/admin',admin_dashboard,name='admin_dashboard'),

    # Matches all url paths so keep at the end of the list
    path('', include('home.urls'))
]
