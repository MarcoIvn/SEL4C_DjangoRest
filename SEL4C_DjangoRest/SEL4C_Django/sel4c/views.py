from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,status
import SEL4C_Django.sel4c.models as models
import SEL4C_Django.sel4c.serializers as serializers
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.admin.models import LogEntry
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.db.models import Count, Max
from . import forms
from .decorators import *
import json


class HomeView(View):
    @method_decorator(staff_required)
    def get(self, request):
        entrepreneurs = models.Entrepreneur.objects.all()
        files_num = models.File.objects.count()
        # Count the number of completed activities for each activity
        activity_counts = models.Activity.objects.annotate(num_completed=Count('activitiescompleted')).values('activity_num', 'num_completed')
        acts_comp_num = models.ActivitiesCompleted.objects.count()
        # Create a dictionary with activity labels and corresponding completion counts
        activity_data = {f"Act. {activity['activity_num']}": activity['num_completed'] for activity in activity_counts}
        recent_actions = LogEntry.objects.all().order_by('-action_time')  
        # Prepare data for the Chartjs graph
        activity_labels = list(activity_data.keys())
        activities_completed = list(activity_data.values())

        # Query to get the count of Entrepreneurs for each gender
        gender_counts = models.Entrepreneur.objects.values('gender').annotate(count=Count('gender'))

        total_entrepreneurs = models.Entrepreneur.objects.count()

        gender_labels = []
        gender_data = []

        for item in gender_counts:
            gender = item['gender']
            count = item['count']
            percentage = (count / total_entrepreneurs) * 100
            gender_labels.append(gender)
            gender_data.append(round(percentage, 2))
        context = {
            'entrepreneurs': entrepreneurs,
            'files_num':files_num,
            'activity_labels': json.dumps(activity_labels),
            'activities_completed': json.dumps(activities_completed),
            'recent_actions': recent_actions,
            'gender_data': json.dumps(gender_data),
            'gender_labels': json.dumps(gender_labels),
            'acts_comp_num':acts_comp_num,
        }   
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
        administrator = models.Administrator.objects.filter(id=id)
        context = { 'administrator': administrator}
        return render(request, "sel4c/user/show.html", context)


class EntrepreneurView(View):
    @method_decorator(staff_required)
    def get(self, request, id):
        # Use Subquery and OuterRef to perform a LEFT JOIN-like operation
        entrepreneur = models.Entrepreneur.objects.get(id = id)
        activities_completed = models.ActivitiesCompleted.objects.filter(entrepreneur=entrepreneur)
        files_uploaded = models.File.objects.filter(entrepreneur=entrepreneur)
        activity_counts = models.Activity.objects.filter(activitiescompleted__entrepreneur=entrepreneur).annotate(num_completed=Count('activitiescompleted')).values('activity_num', 'num_completed')
        activity_data = {f"Actividad {activity['activity_num']}": activity['num_completed'] for activity in activity_counts}

        profile_results_activity1 = models.EntrepreneurProfile.objects.filter(entrepreneur=entrepreneur, activity_id=1).values_list('result1', 'result2', 'result3', 'result4', 'result5', 'result6', 'result7', 'result8', 'result9', 'result10', 'result11', 'result12', 'result13', 'result14', 'result15', 'result16', 'result17')
        profile_results_activity7 = models.EntrepreneurProfile.objects.filter(entrepreneur=entrepreneur, activity_id=7).values_list('result1', 'result2','result3','result4', 'result5', 'result6', 'result7', 'result8', 'result9', 'result10', 'result11', 'result12', 'result13', 'result14', 'result15', 'result16', 'result17')
        ecomplexity_results_activity1 = models.EntrepreneurEcomplexity.objects.filter(entrepreneur=entrepreneur, activity_id=1).values_list('result1', 'result2', 'result3', 'result4')
        ecomplexity_results_activity7 = models.EntrepreneurEcomplexity.objects.filter(entrepreneur=entrepreneur, activity_id=7).values_list('result1', 'result2','result3','result4')
        
        profile_results_activity1 = [[float(item) for item in row] for row in profile_results_activity1]
        profile_results_activity7 = [[float(item) for item in row] for row in profile_results_activity7]
        ecomplexity_results_activity1 = [[float(item) for item in row] for row in ecomplexity_results_activity1]
        ecomplexity_results_activity7 = [[float(item) for item in row] for row in ecomplexity_results_activity7]
        
        print(profile_results_activity1)
        print(profile_results_activity7)
        print(ecomplexity_results_activity1)
        print(ecomplexity_results_activity7)

        activity_labels = list(activity_data.keys())
        activities_completed_list = list(activity_data.values())
        
        activity_answers_files = []
        answers_act1 = []
        answers_act7 = []
        answers_int_labels = []
        answers_str_labels = []
        for activity_completed in activities_completed:
            questions_with_answers = []
            files = []
            for question in models.Question.objects.all():
                answer = question.answer_set.filter(entrepreneur=entrepreneur,activity=activity_completed.activity).first()
                if answer != None:
                    questions_with_answers.append((question, answer))
                    if activity_completed.activity.activity_num == 1:
                        answers_act1.append(answer.answer)
                    elif activity_completed.activity.activity_num == 7:
                        answers_act7.append(answer.answer)
                if question.question_num not in answers_int_labels:
                    answers_int_labels.append(question.question_num)
                    answers_str_labels.append(f"{question.question_num}: {question.description}")
            for file in activity_completed.activity.file_set.filter(entrepreneur=entrepreneur):
                files.append(file)
            activity_answers_files.append((activity_completed, questions_with_answers, files)) 
        
        all_answers = {'answers_act1':answers_act1, 'answers_act7':answers_act7}
        answers_labels = {'answers_int_labels':answers_int_labels, 'answers_str_labels':answers_str_labels}
    
        context = {
            'entrepreneur': entrepreneur,
            'activities_completed': activities_completed,
            'files_uploaded': files_uploaded,
            'activity_answers_files': activity_answers_files,
            'activity_labels': json.dumps(activity_labels),
            'activities_completed_list': json.dumps(activities_completed_list),
            'activities_completed': activities_completed,
            'all_answers': json.dumps(all_answers),
            'answers_labels': json.dumps(answers_labels),
            'profile_results_activity1': json.dumps(profile_results_activity1),
            'profile_results_activity7': json.dumps(profile_results_activity7),
            'ecomplexity_results_activity1' : json.dumps(ecomplexity_results_activity1),
            'ecomplexity_results_activity7' : json.dumps(ecomplexity_results_activity7),
        }
        if request.user.is_authenticated:
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
    messages.success(request, ("Sesión Cerrada Correctamente, hasta pronto."))
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
    queryset = models.Entrepreneur.objects.all()
    serializer_class = serializers.EntrepreneurSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = models.Entrepreneur.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = self.get_queryset()
            if queryset.exists():
                instance = queryset.first()
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return super().list(request, *args, **kwargs)

# http://127.0.0.1:8000/api-root/entrepreneurs/?email=correo@ejemplo.com

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
    def get_queryset(self):
        queryset = models.Question.objects.all()
        activity_id = self.request.query_params.get('activity', None)
        if activity_id is not None:
            queryset = queryset.filter(activity__id=activity_id)
        return queryset

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
    

class ActivitiesCompletedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Respuestas to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.ActivitiesCompleted.objects.all()
    serializer_class = serializers.ActivitiesCompletedSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        entrepreneur_id = self.request.query_params.get('entrepreneur')
        if entrepreneur_id:
            return models.ActivitiesCompleted.objects.filter(entrepreneur=entrepreneur_id)
        return models.ActivitiesCompleted.objects.all()


class CreateMultipleAnswersView(generics.CreateAPIView):
    serializer_class = serializers.AnswerSerializer
    queryset = models.Answer.objects.all()  # Agrega esta línea

    def create(self, request, *args, **kwargs):
        answer_data = request.data.get('answers', [])
        created_answers = []

        for answer_item in answer_data:
            serializer = self.get_serializer(data=answer_item)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            created_answers.append(serializer.data)

        headers = self.get_success_headers(created_answers)
        return Response(created_answers, status=status.HTTP_201_CREATED, headers=headers)


class CreateMultipleQuestionsView(generics.CreateAPIView):
    serializer_class = serializers.QuestionSerializer
    queryset = models.Question.objects.all()  # Agrega esta línea

    def create(self, request, *args, **kwargs):
        print(request)
        question_data = request.data.get('questions', [])
        created_questions = []

        for question_item in question_data:
            serializer = self.get_serializer(data=question_item)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            created_questions.append(serializer.data)

        headers = self.get_success_headers(created_questions)
        return Response(created_questions, status=status.HTTP_201_CREATED, headers=headers)


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
      
# UPDATE Administrator
def editAdministrator(request):
    if request.method == 'POST':
        form = forms.ChangeAdministratorForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Su perfil se ha actualizado!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = forms.ChangeAdministratorForm(instance=request.user)
    return render(request, 'sel4c/user/change_user.html', {'form': form})

# UPDATE Administrator [Password]
def changeAdministratorPassword(request, pk):
    if request.method == 'POST':
        form = forms.ChangeAdministratorPassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = forms.ChangeAdministratorPassword(request.user)
    return render(request, 'sel4c/user/change_password.html', {'form': form})

# DELETE Administrator
class AdministratorDeleteView(DeleteView):
    model = models.Administrator
    template_name = 'sel4c/user/deleteUser.html'
    context_object_name = 'user'
    success_url = '/profile/'


# UPDATE User
@superuser_required
def editOneAdministrator(request,id):
    administrator = get_object_or_404(models.Administrator, id=id)
    if request.method == 'POST':
        form = forms.ChangeAdministratorForm(request.POST, instance=administrator)
        if form.is_valid():
            form.save()
            messages.success(request, 'Administrador actualizado exitosamente.')
            return redirect('administrators')  
    else:
        form = forms.ChangeAdministratorForm(instance=administrator)
    return render(request, 'sel4c/user/edit.html', {"form": form, "administrator": administrator})

@superuser_required
def changeOneAdministratorPassword(request, id):
    administrator = get_object_or_404(models.Administrator, id=id)
    if request.method == 'POST':
        form = forms.ChangeAdministratorPassword(administrator, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contraseña del administrador actualizada exitosamente.')
            return redirect('administrators')  
    else:
        form = forms.ChangeAdministratorPassword(administrator)
    return render(request, 'sel4c/user/change_one_password.html', {'form': form, 'administrator': administrator})

@superuser_required
def deleteOneAdministrator(request, id):
    administrator = get_object_or_404(models.Administrator, id=id)
    administrator.delete()
    messages.success(request, 'Administrador eliminado exitosamente.')
    return redirect('administrators')


def download_file(request, file_id):
    # Retrieve the File object from the database based on the file_id
    file_obj = get_object_or_404(models.File, id=file_id)

    # Open the file and create a FileResponse to serve it for download
    file_path = file_obj.file.path
    response = FileResponse(open(file_path, 'rb'))

    # Set the Content-Disposition header to specify the filename
    response['Content-Disposition'] = f'attachment; filename="{file_obj.file.name}"'

    return response


def fileList(request): 
    files = models.File.objects.all()
    ctx = {
        'files':files}
    return render(request, 'sel4c/files/index.html', ctx)


def listOfEntrepreneurs(request): 
    entrepreneurs = models.Entrepreneur.objects.all()
    ctx = {
        'entrepreneurs':entrepreneurs}
    return render(request, 'sel4c/entrepreneur/index.html', ctx)


def activityList(request): #########################################################
    activities = models.Activity.objects.all()
    ctx = {'activities': activities}
    return render(request, 'sel4c/activities/index.html', ctx)


class ActivityCreateView(CreateView):   
    model = models.Activity
    template_name = 'sel4c/activities/create-edit.html'
    fields = '__all__'
    success_url = '/activities'


class ActivityUpdateView(UpdateView):
    model = models.Activity
    template_name = 'sel4c/activities/create-edit.html'
    fields = '__all__'
    success_url = '/activities'


def questionList(request): #########################################################
    questions = models.Question.objects.all()
    ctx = {'questions': questions}
    return render(request, 'sel4c/questions/index.html', ctx)


class QuestionCreateView(CreateView):   
    model = models.Question
    template_name = 'sel4c/questions/create-edit.html'
    fields = ['activity', 'question_num', 'description']
    success_url = '/questions'


class QuestionUpdateView(UpdateView):
    model = models.Question
    template_name = 'sel4c/questions/create-edit.html'
    fields = '__all__'
    success_url = '/questions'

import csv
import codecs
from django.http import HttpResponse

def csv_all_entrepreneurs_answers(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_entrepreneurs_answers.csv"'

    writer = csv.writer(codecs.getwriter('utf-8')(response))
    writer.writerow(['Actividad', 'Pregunta', 'Emprendedor', 'E-mail', 'Respuesta'])

    answers = models.Answer.objects.all()
    for answer in answers:
        writer.writerow([answer.activity, answer.question, answer.entrepreneur, answer.entrepreneur.email, answer.answer])

    return response


def csv_one_entrepreneur_answers(request, id):
    entrepreneur = models.Entrepreneur.objects.filter(id=id).first()
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{entrepreneur}_answers.csv"'

    writer = csv.writer(codecs.getwriter('utf-8')(response))
    writer.writerow(['Actividad','Pregunta', 'Respuesta'])

    answers = models.Answer.objects.filter(entrepreneur_id=id)
    for answer in answers:
        writer.writerow([answer.activity,answer.question, answer.answer])

    return response

def csv_one_entrepreneur_act_answers(request, id, activity):
    entrepreneur = models.Entrepreneur.objects.filter(id=id).first()
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{entrepreneur}_Act{activity}_answers.csv"'

    writer = csv.writer(codecs.getwriter('utf-8')(response))
    writer.writerow(['Pregunta', 'Respuesta'])

    answers = models.Answer.objects.filter(entrepreneur_id=id, activity=activity)
    for answer in answers:
        writer.writerow([answer.question, answer.answer])

    return response