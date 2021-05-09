from .models import Topics,MCQ
from rest_framework import serializers


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'


class MCQSerializer(serializers.ModelSerializer):

    class Meta:
        model = MCQ
        fields = ['statement','options','correct_ans']
