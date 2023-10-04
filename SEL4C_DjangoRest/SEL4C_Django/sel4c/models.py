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
    #username = models.CharField(primary_key=True, unique=True, default="N/A", max_length=40)
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
        return f"{self.first_name} {self.last_name}"

    class Meta:
        app_label = 'sel4c'
        verbose_name = "Entrepreneurs"
        verbose_name_plural = "Entrepreneurs"

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
    file = models.FileField(upload_to='files/')
    filetype = models.CharField(max_length=255)

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, default=0)

    def __str__(self) -> str:
        return f"{self.id} ({self.activity_id})"
    class Meta:
        app_label = 'sel4c'

class ActivitiesCompleted(models.Model):
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(Entrepreneur,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.activity.activity_num} ({self.entrepreneur})"
    class Meta:
        app_label = 'sel4c'
        verbose_name = "Activities Completed"
        verbose_name_plural = "Activities Completed"

@receiver(post_save, sender=ActivitiesCompleted)
def update_deliveries(sender, instance, created, **kwargs):
    if created:  
        instance.activity.deliveries += 1
        instance.activity.save()
