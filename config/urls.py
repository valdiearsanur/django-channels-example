from django.contrib import admin
from django.urls import path, include

from notifier.views import HomeView


urlpatterns = [
    path('', HomeView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
