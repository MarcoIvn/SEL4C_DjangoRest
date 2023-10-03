from django.contrib.auth.models import User, Group
from django.db.models import OuterRef, Subquery
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
import SEL4C_Django.sel4c.models as models
import SEL4C_Django.sel4c.serializers as serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from . import forms
import json


""" class HomeView(View):
    def get(self, request):
        users = models.Administrator.objects.all()
        entrepreneurs = models.Entrepreneur.objects.all()
        qs = set()
        qs.union(users, entrepreneurs)
        activities = models.Activity.objects.all()

        # activity_labels = [f"Actividad {activity.activity_num}" for activity in activities]
        activity_labels = []
        activity_deliveries = []
        for activity in activities:
            activity_labels.append(f"Actividad {activity.activity_num}")
            activity_deliveries.append(f"{activity.deliveries}")
        
        context = {
            'entrepreneurs': entrepreneurs,
            'activity_labels': json.dumps(activity_labels),
            'activity_deliveries': json.dumps(activity_deliveries)
        }
        print(context)

        if request.user.is_authenticated:
            return render(request, "sel4c/index.html", context)
        else:
            messages.success(request, ("Necesita Iniciar Sesión"))
            return redirect('login')
 """
 
class HomeView(View):
    def get(self, request):
        
        entrepreneurs = models.Entrepreneur.objects.all()

        activities = models.Activity.objects.all()

        # Create the context
        context = {
            'entrepreneurs': entrepreneurs,
            'activity_labels': [f"Actividad {activity.activity_num}" for activity in activities],
            'activity_deliveries': [activity.deliveries for activity in activities],
        }
        print(context)
        if request.user.is_authenticated:
            return render(request, "sel4c/index.html", context)
        else:
            messages.success(request, ("Necesita Iniciar Sesión"))
            return redirect('login')



class EntrepreneurView(View):
    def get(self, request, id):
        users = models.Administrator.objects.filter(is_entrepreneur=True)

        # Use Subquery and OuterRef to perform a LEFT JOIN-like operation
        entrepreneur = models.Entrepreneur.objects.filter(id=OuterRef('id')).only('degree', 'institution', 'gender', 'age', 'country', 'studyField')
        users = users.annotate(
            degree=Subquery(entrepreneur.values('degree')[:1]),
            institution=Subquery(entrepreneur.values('institution')[:1]),
            gender=Subquery(entrepreneur.values('gender')[:1]),
            age=Subquery(entrepreneur.values('age')[:1]),
            country=Subquery(entrepreneur.values('country')[:1]),
            studyField=Subquery(entrepreneur.values('studyField')[:1])
        )

        context = {
            'entrepreneur': users
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
        if user is not None:
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


def registerAdministrator(request):
    if (request.method == 'POST'):
        form = forms.RegisterAdministratorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                messages.error(request, ("Error al crear usuario"))
                return redirect('register')
            else:
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, ("Usuario creado exitosamente"))
                    return redirect('home')
        else:
            return render(request, 'sel4c/register_user.html', {"form": form})
    else:
        form = forms.RegisterAdministratorForm()
        return render(request, 'sel4c/register_user.html', {"form": form})
