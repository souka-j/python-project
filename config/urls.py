from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # API User
    path('admin/', admin.site.urls),
    path('', include('products.urls')),  # 👈 ajoute ça pour inclure l’app products
]
