from django.db import models
from django.contrib.auth.models import User

class GeneratedContent(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.CharField(
        max_length=50
    )

    prompt = models.TextField()

    generated_content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.category
    
class PromptTemplate(models.Model):

    title = models.CharField(
        max_length=100
    )

    category = models.CharField(
        max_length=50
    )

    template = models.TextField()

    def __str__(self):
        return self.title