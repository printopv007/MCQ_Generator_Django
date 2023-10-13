from django.shortcuts import render
from rest_framework import generics
from .serializers import McqSerializer,RandomQuestionSerializer, QuestionSerializer
from mcq.models import Mcqs,Question
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class Mcq(generics.ListAPIView):

    serializer_class=McqSerializer
    queryset = Mcqs.objects.all()



class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(mcq__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question,many=True)
        return Response(serializer.data)

class McqQuestion(APIView):

    def get(self, request,format=None,**kwargs):
        mcq = Question.objects.filter(mcq__title=kwargs['title'])
        serializer = QuestionSerializer(mcq,many=True)
        return Response(serializer.data)