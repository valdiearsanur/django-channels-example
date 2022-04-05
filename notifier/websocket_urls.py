from django.urls import path

from notifier.consumers import ProjectConsumer

urlpatterns = [
    path('ws/collaborators/<str:project_slug>/', ProjectConsumer.as_asgi()),
]
