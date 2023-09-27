from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Admin(AbstractUser):
  username = models.CharField(max_length=40, unique=True)
  email= models.EmailField(max_length=40, unique=True)
  USERNAME_FIELD = "username"
  EMAIL_FIELD = "email"
  is_staff = models.BooleanField(default=False)


  def __str__(self):
      return self.username
  class Meta:
        verbose_name_plural = "admins"

class Entrepreneur(models.Model):
    """ 
    Entrepreneur
    """
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
    activity_num = models.IntegerField()
    title = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.activity_num}"
    class Meta:
        app_label = 'sel4c'


class File(models.Model):
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    file = models.FileField()
    filetype = models.TextField()

    def __str__(self) -> str:
        return f"{self.id} ({self.activity_id})"
    class Meta:
        app_label = 'sel4c'


class Question(models.Model):
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.id}. ({self.description})"
    class Meta:
        app_label = 'sel4c'


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    text = models.TextField(default="N/A")
    username = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, default= "")

    def __str__(self) -> str:
        return f"{self.question_id}.{self.id}"
    class Meta:
        app_label = 'sel4c'

