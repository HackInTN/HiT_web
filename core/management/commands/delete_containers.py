from django.core.management.base import BaseCommand
from django.utils import timezone

from core.container import remove_all_containers

class Command(BaseCommand):
    help = """
           Stop and delete all alive containers.
           This command should be scheduled by a crontab.
           """
    def handle(self, *args, **kwargs):
        remove_all_containers()
        self.stdout.write(self.style.SUCCESS('Deleted all containers [{}]'\
        .format(timezone.now())))
