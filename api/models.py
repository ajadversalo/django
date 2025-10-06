from django.db import models

class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return (self.name or "")
    
class AIQuery(models.Model):
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.question or "") # pylint: disable=invalid-str-returned
    
