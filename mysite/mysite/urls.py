from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('staticpages.urls')),  # Inclui URLs do aplicativo staticpages
    path('accounts/', include('accounts.urls')),  # Inclui URLs do aplicativo accounts
]


