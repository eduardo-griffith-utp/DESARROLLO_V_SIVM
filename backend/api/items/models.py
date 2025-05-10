from django.db import models
class Example(models.Model):
 name = models.CharField(max_length=100)
 description = models.TextField(blank=True, null=True)
 created_at = models.DateTimeField(auto_now_add=True)

 def __str__(self):
    return self.name