from django.contrib.auth.models import User, Group
import SEL4C_Django.sel4c.models as models
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Admin
        fields = ['id','username', 'email', 'first_name', 'last_name']


class EntrepreneurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Entrepreneur
        fields = ['id','username', 'email', 'first_name','last_name', 'degree', 'institution', 'gender', 'age', 'country', 'studyField']


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Activity
        fields = ['id', 'activity_num', 'title', 'description']


class FileSerializer(serializers.HyperlinkedModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(queryset=models.Activity.objects.all())
    class Meta:
        model = models.File
        fields = ['id', 'activity_id', 'file', 'filetype']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(queryset=models.Activity.objects.all())
    class Meta:
        model = models.Question
        fields = ['id', 'activity_id', 'description']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question_id = serializers.PrimaryKeyRelatedField(queryset=models.Question.objects.all())
    class Meta:
        model = models.Answer
        fields = ['id','question_id', 'number', 'text','username']
