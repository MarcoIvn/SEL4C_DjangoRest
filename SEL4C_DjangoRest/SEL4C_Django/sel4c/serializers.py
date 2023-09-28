from django.contrib.auth.models import User, Group
import SEL4C_Django.sel4c.models as models
from django.contrib.auth.models import User, Group
from rest_framework import serializers


""" 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
 """

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['id',
                'username',
                'email',
                'first_name', 
                'last_name',
                'is_staff',
                'is_superuser',
                'is_entrepreneur']


class EntrepreneurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Entrepreneur_Data
        fields = ['user',
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
