from rest_framework import serializers
from rest_framework import serializers
from .models import GeneratedContent
from .models import PromptTemplate

class ContentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedContent
        fields = "__all__"
class GenerateSerializer(serializers.Serializer):

    category = serializers.CharField()

    topic = serializers.CharField()

class PromptTemplateSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = PromptTemplate
        fields = "__all__"