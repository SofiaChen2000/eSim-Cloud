from djongo import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.conf import settings
import uuid


class Task(models.Model):
    # User details for auth to be stored along with task.
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    task_time = models.DateTimeField(auto_now=True, db_index=True)
    task_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)


class spiceFile(models.Model):

    file_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT))
    upload_time = models.DateTimeField(auto_now=True, db_index=True)

    # User details for auth to be stored along with task.
    # owner = models.ForeignKey('auth.User')
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='file')

    def save(self, *args, **kwargs):
        super(spiceFile, self).save(*args, **kwargs)


class runtimeStat(models.Model):
    """
    Stored number of simulations which fall under and between
    each second and the last. For e.g. if a simulation take 0.5s
    to execute then qty field of the row with with exec_time=1
    will increase by 1 (simulations)
    """
    exec_time = models.IntegerField(primary_key=True)
    qty = models.IntegerField(default=0)    

    def __str__(self):
        return str(self.exec_time)

    def save(self, *args, **kwargs):
        super(runtimeStat, self).save(*args, **kwargs)
