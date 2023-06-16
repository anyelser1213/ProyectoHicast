from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('aplicaciones.base_principal.urls')),
    path('', include(('aplicaciones.login.urls'))),
    path('', include(('aplicaciones.usuarios.urls'))),
]
