from django.http import HttpResponse
from rest_framework import generics
from polls.models import Question
from polls.serializers import QuestionSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


