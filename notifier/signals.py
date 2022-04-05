from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import ProjectViewers


@receiver(post_save, sender=User)
def announce_new_user(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gossip", {"type": "user.gossip",
                       "event": "New User",
                       "username": instance.username})

@receiver(post_delete, sender=ProjectViewers)
def post_save_viewer(sender, instance, **kwargs):
    channel_layer = get_channel_layer()

    if instance.is_editor:
        new_viewer = ProjectViewers.objects.switch_editor(instance, instance.project)

        if new_viewer:
            async_to_sync(channel_layer.group_send)(
                'collaboration',
                { 'type': 'broadcast_current_editor' }
            )
