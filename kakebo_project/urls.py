from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kakebo/', include('kakebo_app.urls')),
    path('', include('kakebo_app.urls')),
]