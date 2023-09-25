from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Admin(AbstractUser):
    """ 
    Administrator, inherits from AbstractUser.
    """
    id = models.BigAutoField(default=0, primary_key=True)
    username = models.CharField(max_length=40, unique=True)
    email= models.EmailField(max_length=40, unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    
    username = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = "username"
    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"
    class Meta:
        app_label = 'sel4c'

class Entrepreneur(models.Model):
    """ 
    Entrepreneur
    """
    id = models.BigAutoField(default=0, primary_key=True)
    username = models.CharField(max_length=40, unique=True)
    email = models.CharField(max_length=40, unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    degree = models.TextField()
    institution = models.TextField()
    gender = models.TextField()
    age = models.IntegerField()
    country = models.TextField()
    studyField = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"
    class Meta:
        app_label = 'sel4c'


class Activity(models.Model):
    id = models.BigAutoField(default=0, primary_key=True)
    activity_num = models.IntegerField()
    username = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.activity_num} ({self.username})"
    class Meta:
        app_label = 'sel4c'


class File(models.Model):
    id = models.BigAutoField(default=0, primary_key=True)
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    file = models.FileField()
    filetype = models.TextField()

    def __str__(self) -> str:
        return f"{self.id} ({self.activity_id})"
    class Meta:
        app_label = 'sel4c'


class Question(models.Model):
    id = models.BigAutoField(default=0, primary_key=True)
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.id}. ({self.description})"
    class Meta:
        app_label = 'sel4c'


class Answer(models.Model):
    id = models.BigAutoField(default=0, primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    text = models.TextField(default="N/A")
    
    def __str__(self) -> str:
        return f"{self.question_id}.{self.id}"
    class Meta:
        app_label = 'sel4c'

