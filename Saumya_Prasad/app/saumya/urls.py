from django.contrib import admin
from django.urls import path, include
from saumya_prasad import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('saumya_prasad.urls')),
]
