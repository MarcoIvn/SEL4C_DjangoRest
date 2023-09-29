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

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['id',
                'username',
                'email',
                'password',
                'first_name', 
                'last_name',
                'is_staff',
                'is_superuser',
                'is_entrepreneur']


class EntrepreneurSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(many=False, queryset=models.User.objects.all())
    class Meta:
        model = models.Entrepreneur_Data
        fields = ['id',
                'degree', 
                'institution', 
                'gender', 
                'age', 
                'country', 
                'studyField']
        

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Activity
        fields = ['activity_num', 
                'title', 
                'description', 
                'deliveries']
        
    
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Question
        fields = ['question_num', 
                'activity', 
                'description']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Answer
        fields = ['id_answer',
                'question', 
                'answer', 
                'entrepreneur'] 
        

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.File
        fields = ['id_file',  
                'file', 
                'filetype',
                'activity',
                'entrepreneur']
