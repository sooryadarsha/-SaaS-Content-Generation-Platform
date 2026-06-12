from django.contrib import admin
from django.urls import path, include

from content.views import DeleteContentView, GenerateContentView, ContentHistoryView, PromptTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('users.urls')),

    
    path(
        'generate/',
        GenerateContentView.as_view()
    ),
    path(
        'history/',
        ContentHistoryView.as_view()
    ),

    path(
    'delete/<int:pk>/',
    DeleteContentView.as_view()
),
    path(
    'templates/',
    PromptTemplateView.as_view()
),
]