from django.db import models
import uuid

class Category(models.Model):
    """
        The Category to which each Tool would 

        Belong to.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=30)

class Tool(models.Model):
    """
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)


