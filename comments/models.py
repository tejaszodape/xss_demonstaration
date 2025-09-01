from django.db import models
from django.contrib import admin
# Create your models here.
from django.db import models

class StoredComment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:30]}..."

admin.site.register(StoredComment)