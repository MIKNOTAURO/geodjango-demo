import uuid

from django.contrib.auth.models import User
from django.db import models


class Vet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    certification = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.user.get_full_name()
