# Create your models here.
import uuid  
from django.db import models  
  
  
class NotesModel(models.Model):  
    objects = None  
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    title = models.CharField(max_length=255, unique=True)  
    content = models.TextField()  
    createdAt = models.DateTimeField(auto_now_add=True)  
    updatedAt = models.DateTimeField(auto_now_add=True)  
  
    class Meta:  
        db_table = "notes"  
        ordering = ["createdAt"]  
        constraints = [models.UniqueConstraint(fields=["title"], name="unique_title")]
