from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .gemini_service import generate_ai_content
from .models import GeneratedContent
from .serializers import ContentHistorySerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import DestroyAPIView
from .models import PromptTemplate
from .serializers import PromptTemplateSerializer
from rest_framework.generics import ListAPIView

class GenerateContentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        category = request.data.get("category")
        topic = request.data.get("topic")

        prompt = f"""
        Create a professional {category}
        about {topic}
        """

        generated_text = generate_ai_content(prompt)

        GeneratedContent.objects.create(
            user=request.user,
            category=category,
            prompt=topic,
            generated_content=generated_text
        )

        return Response({
            "success": True,
            "content": generated_text
        })
    
class ContentHistoryView(ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ContentHistorySerializer

    def get_queryset(self):
        return GeneratedContent.objects.filter(
            user=self.request.user
        ).order_by('-created_at')
    

class DeleteContentView(DestroyAPIView):

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GeneratedContent.objects.filter(
            user=self.request.user
        )
    
class PromptTemplateView(
    ListAPIView
):

    queryset = PromptTemplate.objects.all()

    serializer_class = (
        PromptTemplateSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]