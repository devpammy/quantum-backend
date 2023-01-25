from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    todo_name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_todos")


