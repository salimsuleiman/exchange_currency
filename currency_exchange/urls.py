
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views  import *

urlpatterns = [
    path('', Home),
    path('admin/', admin.site.urls),
    path('exchange/', Exchange),
    path('currencies/', include('currencies.urls')),
    path('users/', include('users.urls')),
    path('profits/', Profits),
    path('warehouse/', Exchange)
]
urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)