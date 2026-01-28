from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API
    path('api/events/', include('events.urls')),
    path('api/tickets/', include('tickets.urls')),
    
    # Pages web public - commencent par 'tickets/'
    path('tickets/', include('tickets.urls')),
]
