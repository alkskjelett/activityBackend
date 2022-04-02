from django_filters import rest_framework as filters
from .models import *


# def userCheck(request):
#     if request is None:
#         return User.objects.none()


class TestFilter(filters.FilterSet):
    user = filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Test
        fields = ['user']


class QuestionFilter(filters.FilterSet):
    task = filters.ModelChoiceFilter(queryset=Task.objects.all())

    class Meta:
        model = Question
        fields = ['task']