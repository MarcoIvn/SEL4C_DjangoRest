from django.contrib.auth.models import User, Group
import SEL4C_Django.sel4c.models as models
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.response import Response

""" 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
 """

class AdministratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Administrator
        fields = '__all__'


class EntrepreneurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Entrepreneur
        fields = '__all__'
        

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Activity
        fields = '__all__'
        
    
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    activity = serializers.PrimaryKeyRelatedField(queryset=models.Activity.objects.all())
    class Meta:
        model = models.Question
        fields = '__all__'


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=models.Question.objects.all())
    entrepreneur = serializers.PrimaryKeyRelatedField(queryset=models.Entrepreneur.objects.all())
    class Meta:
        model = models.Answer
        fields = '__all__'
        

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = '__all__'