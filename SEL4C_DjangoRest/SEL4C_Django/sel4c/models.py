from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Administrator(AbstractUser):
    # Inherits id, username, password, first_name, last_name, is_staff, is_superuser
    is_staff = models.BooleanField(default=True)
    def __str__(self):
        return self.username 
    class Meta:
        verbose_name_plural = "Users"


class Entrepreneur(models.Model):
    GENDER_CHOICES = [("Masculino","Masculino"), ("Femenino","Femenino"), ("No binario","No binario"), ("Prefiero no decirlo","Prefiero no decirlo")]
    
    email = models.EmailField(unique=True, max_length=25)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    age = models.IntegerField()
    country = models.CharField(max_length=255)
    studyField = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        app_label = 'sel4c'
        verbose_name = "Entrepreneurs"
        verbose_name_plural = "Entrepreneurs"

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)    
        return super().save(*args, **kwargs)
           

class Activity(models.Model):
    ACTIVITY_CHOICES = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)]

    activity_num = models.IntegerField(choices=ACTIVITY_CHOICES, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.activity_num}"
    class Meta:
        app_label = 'sel4c'


class Question(models.Model):
    question_num = models.IntegerField(default=0)
    description = models.TextField(max_length=250)
    
    def __str__(self) -> str:
        return f"{self.id}. ({self.description})"
    class Meta:
        app_label = 'sel4c'


class Answer(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, default=0)

    def __str__(self) -> str:
        return f"{self.question_id}.{self.id}"
    class Meta:
        app_label = 'sel4c'
        unique_together = ('question', 'entrepreneur','activity')


class File(models.Model):
    file = models.FileField(upload_to='files/')
    filetype = models.CharField(max_length=255)

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, default=0)

    def __str__(self) -> str:
        return f"{self.id} ({self.activity_id})"
    class Meta:
        app_label = 'sel4c'


class ActivitiesCompleted(models.Model):
    attempts = models.SmallIntegerField(default=5)
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(Entrepreneur,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.activity.activity_num} ({self.entrepreneur})"
    class Meta:
        app_label = 'sel4c'
        verbose_name = "Activities Completed"
        verbose_name_plural = "Activities Completed"
        unique_together = ['activity', 'entrepreneur']

class EntrepreneurProfile(models.Model):
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    #date = models.DateField() 
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)
    result1 = models.DecimalField(max_digits=5, decimal_places=2)
    result2 = models.DecimalField(max_digits=5, decimal_places=2)
    result3 = models.DecimalField(max_digits=5, decimal_places=2)
    result4 = models.DecimalField(max_digits=5, decimal_places=2)
    result5 = models.DecimalField(max_digits=5, decimal_places=2)
    result6 = models.DecimalField(max_digits=5, decimal_places=2)
    result7 = models.DecimalField(max_digits=5, decimal_places=2)
    result8 = models.DecimalField(max_digits=5, decimal_places=2)
    result9 = models.DecimalField(max_digits=5, decimal_places=2)
    result10 = models.DecimalField(max_digits=5, decimal_places=2)
    result11 = models.DecimalField(max_digits=5, decimal_places=2)
    result12 = models.DecimalField(max_digits=5, decimal_places=2)
    result13 = models.DecimalField(max_digits=5, decimal_places=2)
    result14 = models.DecimalField(max_digits=5, decimal_places=2)
    result15 = models.DecimalField(max_digits=5, decimal_places=2)
    result16 = models.DecimalField(max_digits=5, decimal_places=2)
    result17 = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Resultados Perfil Emprendedor para {self.entrepreneur}"
    
class EntrepreneurEcomplexity(models.Model):
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    #date = models.DateField() 
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)
    result1 = models.DecimalField(max_digits=5, decimal_places=2)
    result2 = models.DecimalField(max_digits=5, decimal_places=2)
    result3 = models.DecimalField(max_digits=5, decimal_places=2)
    result4 = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Resultados E-Complexity para {self.entrepreneur}"

def processEntrepreneurProfileAnswers(answers):
    results = []
    entrepreneur_answers = list(answers.order_by('id').values_list('answer', flat=True))

    results.append(entrepreneur_answers[0])  # Value of the first question
    results.append(sum(entrepreneur_answers[1:3]) / 2)  # Average of the second and third question

    results.append(entrepreneur_answers[3])  # Value of the fourth question
    results.append(entrepreneur_answers[4])  # Value of the fifth question

    results.append(sum(entrepreneur_answers[5:7]) / 2)  # Average of the sixth and seventh question
    results.append(sum(entrepreneur_answers[7:9]) / 2)  # Average of the eighth and ninth question

    results.append(entrepreneur_answers[9])  # Value of the tenth question
    results.append(sum(entrepreneur_answers[10:12]) / 2)  # Average of the eleventh and twelfth question

    results.append(entrepreneur_answers[12])  # Value of the thirteenth question
    results.append(sum(entrepreneur_answers[13:15]) / 2)  # Average of the fourteenth and fifteenth question

    results.append(entrepreneur_answers[15])  # Value of the sixteenth question
    results.append(entrepreneur_answers[16])  # Value of the seventeenth question

    results.append(entrepreneur_answers[17])  # Value of the eighteenth question

    results.append(sum(entrepreneur_answers[18:21]) / 3)  # Average of the nineteenth, twentieth, and twenty-first question

    results.append(entrepreneur_answers[21])  # Value of the twenty-second question
    results.append(entrepreneur_answers[22])  # Value of the twenty-third question
    results.append(entrepreneur_answers[23])  # Value of the twenty-fourth question

    return results

def processEntrepreneurEcomplexityAnswers(answers):
    results = []
    entrepreneur_answers = list(answers.order_by('id').values_list('answer', flat=True))

    results.append(sum(entrepreneur_answers[24:30]) / 6)  # Promedio del grupo 25-30
    results.append(sum(entrepreneur_answers[30:37]) / 7)  # Promedio del grupo 31-37
    results.append(sum(entrepreneur_answers[37:43]) / 6)  # Promedio del grupo 38-43
    results.append(sum(entrepreneur_answers[43:49]) / 6)  # Promedio del grupo 44-49

    return results


@receiver(post_save, sender=ActivitiesCompleted)
def process_activity_completion(sender, instance, created, **kwargs):
    if created and (instance.activity.id == 1 or instance.activity.id == 7):
        entrepreneur = instance.entrepreneur
        activity_id = instance.activity.id
        answers = Answer.objects.filter(entrepreneur=entrepreneur, activity=activity_id)
        
        results = processEntrepreneurProfileAnswers(answers)
        entrereneur_profile = EntrepreneurProfile.objects.create(
            entrepreneur=entrepreneur,
            #date=instance.date,
            activity_id=activity_id,  
            result1=results[0],
            result2=results[1],
            result3=results[2],
            result4=results[3],
            result5=results[4],
            result6=results[5],
            result7=results[6],
            result8=results[7],
            result9=results[8],
            result10=results[9],
            result11=results[10],
            result12=results[11],
            result13=results[12],
            result14=results[13],
            result15=results[14],
            result16=results[15],
            result17=results[16]
        )
        results = processEntrepreneurEcomplexityAnswers(answers)

        entrepreneur_ecomplexity = EntrepreneurEcomplexity.objects.create(
            entrepreneur=entrepreneur,
            #date=instance.date,
            activity_id=activity_id,  
            result1=results[0],
            result2=results[1],
            result3=results[2],
            result4=results[3],
        )


