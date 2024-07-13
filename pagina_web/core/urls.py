from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    	path('',index,name="index"),
        path('libro/',Libros,name="libro"),
        path('autor',Autores,name="autor"),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)