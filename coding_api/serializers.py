from .models import Topics,MCQ,Options
from rest_framework import serializers


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'



class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Options
        fields = ['A','B','C','D']


class MCQSerializer(serializers.ModelSerializer):

    options = OptionsSerializer(many=True,read_only=True)

    class Meta:
        model = MCQ
        fields = ['statement','options','correct_ans']
