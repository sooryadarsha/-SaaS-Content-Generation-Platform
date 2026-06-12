from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    GeneratedContent,
    PromptTemplate
)

admin.site.register(GeneratedContent)
admin.site.register(PromptTemplate)