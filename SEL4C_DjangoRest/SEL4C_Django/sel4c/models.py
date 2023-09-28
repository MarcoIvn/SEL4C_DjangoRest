from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
  is_admin = models.BooleanField(default=False)

  def __str__(self):
      return self.username 
  class Meta:
        verbose_name_plural = "Users"


class Entrepreneur(Usuario):
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)
    studyField = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"
    class Meta:
        app_label = 'sel4c'
        verbose_name = "Entrepreneur"
        verbose_name_plural = "Entrepreneurs"


class Activity(models.Model):
    id_activity = models.BigAutoField(primary_key=True)
    activity_num = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deliveries = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.activity_num}"
    class Meta:
        app_label = 'sel4c'


class Question(models.Model):
    id_question = models.BigAutoField(primary_key=True)
    question_num = models.IntegerField(default=0)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.id}. ({self.description})"
    class Meta:
        app_label = 'sel4c'


class Answer(models.Model):
    id_answer = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)

    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, null="N/A")

    def __str__(self) -> str:
        return f"{self.question_id}.{self.id}"
    class Meta:
        app_label = 'sel4c'


class File(models.Model):
    id_file = models.BigAutoField(primary_key=True)
    file = models.FileField(upload_to='files/')
    filetype = models.CharField(max_length=255)

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, null="N/A")

    def __str__(self) -> str:
        return f"{self.id} ({self.activity_id})"
    class Meta:
        app_label = 'sel4c'
