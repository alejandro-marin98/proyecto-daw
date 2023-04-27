from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from login import views as log
from solicitudes import views as sol


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('libros/', include('gestionLibros.urls')),
    path('login/', include('login.urls')),
    path('solicitudes/', include('solicitudes.urls')),
    path('getSolicitudes/<str:username>/', sol.getSolicitudes),
    path('profile/', log.profile),
    path('friends/', log.friends),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
