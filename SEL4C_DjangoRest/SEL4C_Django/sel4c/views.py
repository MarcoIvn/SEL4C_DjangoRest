from django.contrib.auth.models import User, Group
from django.db.models import OuterRef, Subquery
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
import SEL4C_Django.sel4c.models as models
import SEL4C_Django.sel4c.serializers as serializers
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .decorators import *
from django.utils.decorators import method_decorator
from . import forms
import json


class HomeView(View):
    @method_decorator(staff_required)
    def get(self, request):
        entrepreneurs = models.Entrepreneur.objects.all()
        activities = models.Activity.objects.all()
        context = {
            'entrepreneurs': entrepreneurs,
            'activity_labels': [f"Actividad {activity.activity_num}" for activity in activities],
            'activity_deliveries': [activity.deliveries for activity in activities],
        }
        print(context)
        return render(request, "sel4c/index.html", context)


class AdministratorsView(View):
    @method_decorator(superuser_required)
    def get(self, request):
        administrators = models.Administrator.objects.all()
        context = { 'administrators': administrators}
        return render(request, "sel4c/user/index.html", context)
    
  
class AdministratorView(View):
    @method_decorator(superuser_required)
    def get(self, request, id):
        administrator = models.Administrator.objects.filter(id = id)
        context = { 'administrator': administrator}
        print(context)
        return render(request, "sel4c/user/show.html", context)



class EntrepreneurView(View):
    @method_decorator(staff_required)
    def get(self, request, id):
        # Use Subquery and OuterRef to perform a LEFT JOIN-like operation
        entrepreneur = models.Entrepreneur.objects.filter(id = id)
        context = {
            'entrepreneur': entrepreneur
        }
        print(context)
        if request.user.is_authenticated and entrepreneur.exists:
            return render(request, "sel4c/entrepreneur/show.html", context)
        else:
            return render(request, "sel4c/index.html")


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
          return redirect('home')
        return render(request, 'authentication/login.html', {})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('home')
        else:
            messages.success(
            request, ("Nombre de usuario o contraseña incorrectos, Intentelo de nuevo"))
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
    queryset = models.Administrator.objects.all()
    serializer_class = serializers.AdministratorSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class EntrepreneurViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    # permission_classes = [permissions.IsAuthenticated]
    queryset = models.Entrepreneur.objects.all()
    serializer_class = serializers.EntrepreneurSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Actividades to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Archivos to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Preguntas to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Respuestas to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class registerAdministrator(View):
    @method_decorator(superuser_required)
    def get(self,request):
        form = forms.RegisterAdministratorForm()
        return render(request, 'sel4c/user/new.html', {"form": form})
    @method_decorator(superuser_required)
    def post(self, request):
        form = forms.RegisterAdministratorForm(request.POST)
        if form.is_valid():
          try:
            form.save()
          except:
            messages.error(request, ("Error al crear usuario"))
            return redirect('register')
          else:
            #username = form.cleaned_data["username"]
            #password = form.cleaned_data["password1"]
            messages.success(request, ("Usuario creado exitosamente"))
            return redirect('home')
        else:
          return render(request, 'sel4c/user/new.html', {"form": form})
      
# UPDATE User
@superuser_required
def editAdministrator(request,id):
    administrator = get_object_or_404(models.Administrator, id=id)
    if request.method == 'POST':
        form = forms.RegisterAdministratorForm(request.POST, instance=administrator)
        if form.is_valid():
            form.save()
            messages.success(request, 'Administrador actualizado exitosamente.')
            return redirect('home')  
    else:
        form = forms.RegisterAdministratorForm(instance=administrator)
        return render(request, 'sel4c/user/edit.html', {"form": form, "administrator": administrator})

@superuser_required
def deleteAdministrator(request, id):
    administrator = get_object_or_404(models.Administrator, id=id)
    administrator.delete()
    messages.success(request, 'Administrador eliminado exitosamente.')
    return redirect('administrators')  

