from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('accounts/', include('accounts.urls', namespace='accounts')),
                  path('', include('shop.urls', namespace='shop')),
                  path('cart/', include('cart.urls', namespace='cart')),
                  path('orders/', include('orders.urls', namespace='orders')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
