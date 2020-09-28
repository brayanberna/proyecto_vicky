from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('export_excel.urls')),
    path('', include('export_calculos.urls')),
]
