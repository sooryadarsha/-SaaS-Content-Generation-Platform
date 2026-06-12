from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from content.models import GeneratedContent


class DashboardStatsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        contents = GeneratedContent.objects.filter(
            user=request.user
        )

        return Response({
    "total_contents": contents.count(),

    "blogs": contents.filter(
        category="Blog"
    ).count(),

    "emails": contents.filter(
        category="Email"
    ).count(),

    "social_posts": contents.filter(
        category="Social"
    ).count(),

    "marketing_contents": contents.filter(
        category="Marketing"
    ).count(),
})