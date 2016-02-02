from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser


class Challenge(models.Model):
    name = models.CharField(max_length=80)
    flag = models.CharField(max_length=80, null=True)
    value = models.IntegerField()
    description = models.TextField()
    docker_name = models.CharField(max_length=80)

    @property
    def dict(self):
        return {
            'id' : int(self.id),
            'name' : str(self.name),
            'description' : str(self.description),
        }

    def getFullDict(self, user):
        d = self.dict
        d['active'] = user.isActive(self)
        d['validated'] = user.isValidated(self)
        return d

    def __str__(self):
        return self.name

class Container(models.Model):
    docker_id = models.CharField(unique=True, null=True, max_length=80)
    creation_date = models.DateTimeField(null=True)
    challenge = models.ForeignKey(Challenge)

    def __str__(self):
        return str(self.docker_id)

class User(AbstractUser):
    score = models.IntegerField(default=0)
    creation_date = models.DateTimeField(null=True)
    validation_key = models.UUIDField(default=uuid4)
    container = models.OneToOneField(Container, null=True,
                                     on_delete=models.DO_NOTHING)
    solved = models.ManyToManyField(Challenge)

    @property
    def dict(self):
        return {
            'id' : self.id,
            'username' : str(self.username),
            'creation_date' : str(self.creation_date),
            'score' : int(self.score)
        }

    def isActive(self, challenge):
        return self.container is not None and \
        self.container.challenge == challenge

    def isValidated(self, challenge):
        return self.solved.filter(pk=challenge.pk).exists()
