from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from .flag_validation import crypt_b64

class Challenge(models.Model):
    name = models.CharField(max_length=80)
    flag = models.CharField(max_length=16, null=True)
    value = models.IntegerField()
    description = models.TextField()
    docker_name = models.CharField(max_length=80, null=True, blank=True)
    is_docker = models.BooleanField()
    is_binary = models.BooleanField()

    @property
    def dict(self):
        return {
            'id' : int(self.id),
            'name' : str(self.name),
            'description' : str(self.description),
            'value' : int(self.value),
            'is_docker' : bool(self.is_docker),
            'is_binary' : bool(self.is_binary)
        }

    def getFullDict(self, user):
        d = self.dict
        d['active'] = user.isActive(self)
        d['validated'] = user.isValidated(self)
        return d

    def getEncryptedFlag(self, user):
        return crypt_b64(user.validation_key.bytes,
                       str(self.flag).encode())

    def check_flag(self, user, string):
        if bool(self.is_docker):
            return string == str(self.flag) #TODO: crypted docker flag
        elif bool(self.is_binary):
            return self.getEncryptedFlag(user) == string.encode()
        else:
            return string == str(self.flag)

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
    container = models.OneToOneField(Container, null=True, blank=True,
                                     on_delete=models.SET_NULL)
    solved = models.ManyToManyField(Challenge, blank=True)

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
