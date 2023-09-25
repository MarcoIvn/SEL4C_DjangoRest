from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
import SEL4C_Django.sel4c.models as models
import SEL4C_Django.sel4c.serializers as serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

class HomeView(View):
  def get(self,request):
    entrepreneurs = models.Entrepreneur.objects.all()  # Recupera todos los objetos Entrepreneur
    context = {'entrepreneurs': entrepreneurs}
    if request.user.is_authenticated:
      return render(request, "sel4c/index.html", context)
    else:
      messages.success(request, ("Necesita Iniciar Sesión"))
      return redirect('login')
    
  
class LoginView(View):
  def get(self, request):
    if request.user.is_authenticated:
      return redirect('home')
    return render(request, 'authentication/login.html', {})

  def post(self, request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.success(request, ("Nombre de usuario o contraseña incorrectos, Intentelo de nuevo"))
      return redirect('login')
    
def logoutView(request):
  logout(request)
  messages.success(request, ("Sesión Cerrada Correctamente, bye!!!"))
  return redirect('login')

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