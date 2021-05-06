from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from rest_framework.response import Response
import json
from .models import Options,Topics,MCQ
from django.db import DatabaseError, transaction
from .serializers import TopicSerializer,MCQSerializer,OptionsSerializer
# Create your views here.


def welcome(request):
    return JsonResponse({'status':'Working..'})


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def help(request):
    u={
        'all_topics':'/all-topics/',
    }


    return Response(u)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def all_topics(request):
    topics = Topics.objects.all()
    serializer = TopicSerializer(topics,many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def complete_topic(request,topic_id):
    mcq = MCQ.objects.filter(topic_id=topic_id)
    mcq = MCQSerializer(mcq,many=True)
    return Response(mcq.data)








def fill_DB(request):
    topics = Topics.objects.all()
    for t in topics:
        t.total_mcq = MCQ.objects.filter(topic_id=t.topic_id).count()
        t.save()
        
    
    '''
    with open('mcqs.json','r') as f:
        dataset = json.load(f)
        print('Started addding to DB')
        for i in range(dataset.get('total_topics')):
            print(f'value of i {i}')
            topic_mcq = dataset.get(str(i))
            topic_name=topic_mcq.get('topic_name')
            mcq = topic_mcq.get('mcqs')
            
            for key,value in mcq.items():
                stmt = value.get('statement')
                options = value.get('options')
                a=options.get('a')
                b=options.get('b')
                c=options.get('c')
                d=options.get('d')
                correct_ans = value.get('correct')
                try:
                    with transaction.atomic():
                        topic , _ = Topics.objects.get_or_create(topic_name=topic_name)
                        topic.save()
                        topic = Topics.objects.get(topic_id=topic.topic_id)
                        print('topic saved')
                        mcq = MCQ.objects.create(topic_id=topic,statement=stmt,correct_ans=correct_ans)
                        mcq.save()
                        
                        mcq = MCQ.objects.get(mcq_id=mcq.mcq_id)

                        options = Options.objects.create(mcq_id=mcq,A=a,B=b,C=c,D=d)
                        options.save()
                        print('options saved')
                        print(f'saved key = {key} of  topics={topic_name} ')
                except DatabaseError:
                    print('ERROORRRR: ===========')
    '''
        
    return JsonResponse({'done':'True'})

