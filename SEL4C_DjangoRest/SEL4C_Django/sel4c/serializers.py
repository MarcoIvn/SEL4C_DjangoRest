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
        fields = [
                'id',
                'email',
                'password',
                'first_name',
                'last_name',
                'degree', 
                'institution', 
                'gender', 
                'age', 
                'country', 
                'studyField']
        

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Activity
        fields = [
                'id',
                'activity_num', 
                'title', 
                'description', 
                'deliveries']
        
    
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    activity = serializers.PrimaryKeyRelatedField(queryset=models.Activity.objects.all())
    class Meta:
        model = models.Question
        fields = [
                'id',
                'question_num', 
                'activity', 
                'description']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    activity = serializers.PrimaryKeyRelatedField(queryset=models.Activity.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=models.Question.objects.all())
    entrepreneur = serializers.PrimaryKeyRelatedField(queryset=models.Entrepreneur.objects.all())
    class Meta:
        model = models.Answer
        fields = ['id',
                'activity',
                'question', 
                'answer', 
                'entrepreneur'] 
        

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = ['id',  
                'file', 
                'filetype',
                'activity',
                'entrepreneur']
        

class ActivitiesCompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActivitiesCompleted
        fields = ['id','activity','entrepreneur','attempts']