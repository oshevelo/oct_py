from django.http import HttpResponse
from rest_framework import generics
from rest_framework.exceptions import NotAcceptable
from apps.polls.models import Question
from apps.polls.api.serializers import QuestionSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, *args, **kwargs):
        if  'limit' not in self.request.GET or  'offset' not in self.request.GET:
            raise NotAcceptable('asdasdas')
        return super().get(*args, **kwargs)


