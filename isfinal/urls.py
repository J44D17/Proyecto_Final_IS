# from django.contrib import admin
from django.urls import path, include
# sirve para acceder a todas las variables definidas en el archivo settings
from django.conf import settings
# sirve para cargar un grupo de rutas estaticas
from django.conf.urls.static import static
# vista predeterminada que sirve para generar la JWT
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('cms/', include('cms.urls')),
    path('login', TokenObtainPairView.as_view()),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
