import uuid

from django.db import models

from account.models import User

class Project(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True, null = True)
    created_by = models.ForeignKey(User, related_name = 'projects', on_delete = models.CASCADE)

    def __str__(self):
        return self.name