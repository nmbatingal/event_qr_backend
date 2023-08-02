import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    events = models.ManyToManyField('Event', related_name='participants')
    updated = models.DateTimeField(auto_now=True)
    qr_code = models.CharField(max_length=200, editable=False, null=True, blank=True)
    
    # Add other fields as needed
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.qr_code: # This is a new object
            self.qr_code = f"{self.id}"
        super(User, self).save(*args, **kwargs)


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField(null=True, blank=True)
    # Add other fields as needed
    