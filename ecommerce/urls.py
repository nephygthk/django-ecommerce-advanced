from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerce.core.urls', namespace='core')),
    path('store/', include('ecommerce.store.urls', namespace='store')),
]