from rest_framework import viewsets, permissions
from .serializers import *
from .filter import *
from django_filters.rest_framework  import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category__title']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionSerializer
    # filterset_class = QuestionFilter
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['task']


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TestSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['task']
    # filterset_class = TestFilter


class AnswerQuestionViewSet(viewsets.ModelViewSet):
    queryset = AnswerQuestion.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnswerQuestionSerializer
