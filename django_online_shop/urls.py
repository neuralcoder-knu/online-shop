from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('accounts/', include('accounts.urls', namespace='accounts'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
