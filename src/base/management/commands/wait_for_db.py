# This will required if we run using docker
# In this project we do not have a database so no need
import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to pass execution  until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 sec...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
