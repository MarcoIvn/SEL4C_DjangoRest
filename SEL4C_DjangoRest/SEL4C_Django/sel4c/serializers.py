import SEL4C_Django.sel4c.models as models
from rest_framework import serializers
from rest_framework.response import Response

from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry
""" 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
 """
@receiver(pre_save, sender=models.Entrepreneur)  # Reemplaza YourModel con el modelo que deseas rastrear
def log_action(sender, instance, **kwargs):
    content_type = ContentType.objects.get_for_model(instance)
    
    if instance._state.adding:
        action_flag = 1  # 1 para adición
    else:
        action_flag = 2  # 2 para modificación

    LogEntry.objects.log_action(
        user_id=1,  # Reemplaza instance.user.id con el usuario que realizó la acción
        content_type_id=content_type.id,
        object_id=instance.pk,
        object_repr=str(instance),
        action_flag=action_flag
    )

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