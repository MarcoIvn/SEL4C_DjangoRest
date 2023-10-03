from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.

class Administrator(AbstractUser):
    # Inherits id, username, password, first_name, last_name, is_staff, is_superuser
    def __str__(self):
        return self.username 
    class Meta:
        verbose_name_plural = "Users"


class Entrepreneur(models.Model):
    username = models.CharField(primary_key=True, unique=True, default="N/A", max_length=40)
    email = models.EmailField(unique=True, max_length=25)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)
    studyField = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.username}"

    class Meta:
        app_label = 'sel4c'
        verbose_name = "Entrepreneur's Data"
        verbose_name_plural = "Entrepreneurs' Data"

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)    
        return super().save(*args, **kwargs)
           
    
    

class Activity(models.Model):
    activity_num = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deliveries = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.activity_num}"
    class Meta:
        app_label = 'sel4c'


class Question(models.Model):
    question_num = models.IntegerField(default=0)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.id}. ({self.description})"
    class Meta:
        app_label = 'sel4c'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(default=0)

    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, default=0)

    def __str__(self) -> str:
        return f"{self.question_id}.{self.id}"
    class Meta:
        app_label = 'sel4c'


class File(models.Model):
    id_file = models.BigAutoField(primary_key=True)
    file = models.FileField(upload_to='files/')
    filetype = models.CharField(max_length=255)

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, default=0)

    def __str__(self) -> str:
        return f"{self.id} ({self.activity_id})"
    class Meta:
        app_label = 'sel4c'
