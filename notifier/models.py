from django.db import models
from django.contrib.auth.models import User


class ProjectViewersManager(models.Manager):
    def switch_editor(self, previous_editor, project):
        potential_editor = self.get_queryset().filter(project=project).order_by('timestamp').first()
        if potential_editor:
            potential_editor.status = ProjectViewers.STATUS_EDITOR
            potential_editor.save()

            return potential_editor

    def set_editor_or_viewer(self, project, user):
        status = ProjectViewers.STATUS_VIEWER
        if not self.has_editor(project):
            status = ProjectViewers.STATUS_EDITOR
        
        return self.get_or_create(project=project, user=user, defaults={'status': status})

    def remove(self, project, user):
        self.get_queryset().filter(project=project, user=user).delete()

    def has_editor(self, project):
        return self.get_queryset().filter(project=project, status=ProjectViewers.STATUS_EDITOR).count() > 0

    def get_editor(self, project):
        return self.get_queryset().filter(project=project, status=ProjectViewers.STATUS_EDITOR).first()

    def get_editor_username(self, project):
        editor = self.get_editor(project)
        if editor:
            return editor.user.username
        return None


# Create your models here.
class ProjectViewers(models.Model):
    STATUS_EDITOR = 'editor'
    STATUS_VIEWER = 'viewer'
    STATUS_IDDLE = 'iddle'

    project = models.CharField(max_length=256)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProjectViewersManager()

    @property
    def is_editor(self):
        return self.status == ProjectViewers.STATUS_EDITOR

    # class Meta:
    #     unique_together = ('project', 'status',)
