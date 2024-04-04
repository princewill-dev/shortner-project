import string
import random
from django.db import models
from django.contrib.auth.models import AbstractUser

def generate_account_id():
    characters = string.ascii_letters + string.digits
    account_id = ''.join(random.choice(characters) for _ in range(12))
    return account_id

class User(AbstractUser):
    account_id = models.CharField(max_length=12, unique=True, default=generate_account_id)
    email = models.EmailField(unique=True)

# class User(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=200)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=200)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.name}"