from asgiref.sync import async_to_sync

from channels.generic.websocket import JsonWebsocketConsumer

from .models import ProjectViewers

class ProjectConsumer(JsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super(ProjectConsumer, self).__init__(*args, **kwargs)
        self.project_slug = None
        self.project = None
        self.user = None
        self.viewer = None

    def get_project(self, scope):
        project_slug = scope['url_route']['kwargs']['project_slug']
        return project_slug

    def get_user(self, scope):
        user = scope['user']
        if user and user.is_authenticated:
            return user._wrapped
        return None

    def project_collaborator(self, event):
        self.send_json(event)

    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)("collaboration", self.channel_name)

        self.project = self.get_project(self.scope)
        self.user = self.get_user(self.scope)

        if not self.project or not self.user:
            return

        async_to_sync(self.channel_layer.group_send)(
            'collaboration',
            {
                'type': 'project_collaborator',
                'event': 'find_editor',
                'username': ProjectViewers.objects.get_editor_username(self.project)
            }
        )

        self.viewer = ProjectViewers.objects.set_editor_or_viewer(self.project, self.user)

        print(f"*** Added {self.channel_name} channel to collaboration")

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("collaboration", self.channel_name)

        if not self.project or not self.user:
            return

        self.viewer = ProjectViewers.objects.remove(self.project, self.user)

        print(f"*** Removed {self.channel_name} channel to collaboration")

    def receive(self, text_data=None, bytes_data=None):

        if not self.project or not self.user:
            return
