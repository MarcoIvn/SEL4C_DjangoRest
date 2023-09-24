from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
import SEL4C_Django.sel4c.models as models
import SEL4C_Django.sel4c.serializers as serializers


""" class UserViewSet(viewsets.ModelViewSet):
    
    API endpoint that allows users to be viewed or edited.
    
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
 
    API endpoint that allows groups to be viewed or edited.

    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
 """

class AdminViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer

class EntrepreneurViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Entrepreneur.objects.all()
    serializer_class = serializers.EntrepreneurSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Actividades to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer


class FileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Archivos to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Preguntas to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Respuestas to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer